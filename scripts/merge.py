import os
import glob
import json
import nbformat

kernel_file = json.load(open(os.path.join("kernel-metadata.json")))

SOURCE_FOLDER = "milestones"
TARGET_NOTEBOOK = "competition.ipynb"
OUTPUT_NOTEBOOK = kernel_file["code_file"]


def demote_headers(nb):
    """
    Iterates through all cells in the notebook.
    If a cell is markdown, it prepends '#' to any line starting with '#'.
    """
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            lines = cell.source.splitlines()
            new_lines = []
            for line in lines:
                stripped = line.lstrip()
                if stripped.startswith("#"):
                    new_lines.append("#" + line)
                else:
                    new_lines.append(line)
            cell.source = "\n".join(new_lines)
    return nb


def merge_notebooks():
    """
    Merges all notebooks in the SOURCE_FOLDER into a single notebook.
    It adds a markdown cell at the top with an automated merge message and a code cell to
    stop execution. It also adds a 'Milestones' markdown cell before merging the content of the notebooks.
    """
    if os.path.exists(TARGET_NOTEBOOK):
        with open(TARGET_NOTEBOOK, "r", encoding="utf-8") as f:
            master_nb = nbformat.read(f, as_version=4)
    else:
        print(f"{TARGET_NOTEBOOK} not found. Creating a new one.")
        master_nb = nbformat.v4.new_notebook()

    notebook_files = sorted(glob.glob(os.path.join(SOURCE_FOLDER, "*.ipynb")))

    if not notebook_files:
        print("No notebooks found to merge.")
        return

    auto_msg_source = (
        "--- \n"
        "**⚠️ Automated Merge Info**\n\n"
        "The cells below were added automatically by the merge script to control execution flow."
    )
    master_nb.cells.append(nbformat.v4.new_markdown_cell(auto_msg_source))

    # "Stop Execution" code cell
    stop_source = "# stop execution here\n\n" "import sys\n" "sys.exit(0)"
    stop_cell = nbformat.v4.new_code_cell(stop_source)
    master_nb.cells.append(stop_cell)

    # 'Milestones' markdown cell
    milestone_cell = nbformat.v4.new_markdown_cell("# Milestones")
    master_nb.cells.append(milestone_cell)

    for nb_file in notebook_files:
        print(f"Merging: {nb_file}")
        with open(nb_file, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            nb = demote_headers(nb)
            master_nb.cells.extend(nb.cells)

    # Save
    with open(OUTPUT_NOTEBOOK, "w", encoding="utf-8") as f:
        nbformat.write(master_nb, f)

    print(f"Successfully merged notebooks into {OUTPUT_NOTEBOOK}")


if __name__ == "__main__":
    merge_notebooks()
