# Comment Category Prediction Challenge

This project focuses on predicting the category of comments based on their content and associated metadata. It was developed as part of a machine learning challenge to classify comments into four distinct internal handling categories.

## Project Overview

The goal is to build a robust multiclass classification model that can accurately categorize comments using a variety of features, including raw text, engagement metrics (upvotes/downvotes), and internal platform-specific indicators.

## Dataset Description

The dataset consists of approximately 198,000 training samples and 102,000 test samples.

### Data Files
- `datasets/train.csv`: Training set with labels.
- `datasets/test.csv`: Test set for which predictions are required.
- `datasets/sample_submission.csv`: Sample format for submissions.

### Features
- **comment**: The raw text content of the comment.
- **created_date**: Timestamp of the comment.
- **post_id**: Identifier for the parent discussion thread.
- **upvote / downvote**: Engagement metrics.
- **emoticon_1, 2, 3**: Indicators for different groups of emoticons.
- **if_1, if_2**: Internal platform features.
- **race, religion, gender, disability**: Indicators for specific topics detected by the system.
- **label**: The target variable (0, 1, 2, or 3).

## Methodology

### 1. Preprocessing
- **Text Cleaning**: Removal of URLs, special characters, and extra whitespaces. Lowercasing of all text.
- **Handling Missing Values**: Specific handling for categorical indicators like `race`, `religion`, and `gender`.

### 2. Feature Engineering
- **TF-IDF Vectorization**: Converting cleaned text into numerical features using `TfidfVectorizer`.
- **Numerical Features**: Scaling of engagement metrics and internal flags.

### 3. Modeling
- **Models Used**: Gradient Boosting machines, specifically **LightGBM** and **XGBoost**.
- **Cross-Validation**: 5-fold Stratified K-Fold validation to ensure model stability and prevent overfitting.

## Technology Stack
- **Language**: Python
- **Data Manipulation**: Pandas, NumPy
- **Machine Learning**: Scikit-learn, LightGBM, XGBoost
- **Visualization**: Matplotlib, Seaborn
- **Environment**: Jupyter Notebook / Kaggle Kernels

## Project Rules

Only the following libraries were allowed to be used in the competition:

1.  [NumPy](https://numpy.org/doc/stable/user/index.html)
2.  [Pandas](https://pandas.pydata.org/docs/user_guide/index.html)
3.  [Matplotlib](https://matplotlib.org/stable/users/index)
4.  [Scikit-learn](https://scikit-learn.org/stable/supervised_learning.html)
5.  [XGBoost](https://xgboost.readthedocs.io/en/latest/install.html)
6.  [Seaborn](https://seaborn.pydata.org/)
7.  [Imblearn](https://imbalanced-learn.org/stable/)
8.  [SciPy](https://docs.scipy.org/doc/scipy/tutorial/index.html)
9.  [Pickle](https://docs.python.org/3/library/pickle.html)
10. [regex](https://docs.python.org/3/library/re.html)
11. [Lightgbm](https://lightgbm.readthedocs.io/en/stable/)
12. [Plotly](https://plotly.com/)
13. [statsmodel](https://www.statsmodels.org/stable/index.html)

**Note:** These libraries are already installed in your Kaggle notebook. Python in-built libraries can also be used. *Using libraries like TensorFlow, PyTorch, NLTK, word2vec, textblob etc is **NOT** allowed*.

## Setup and Usage

### Prerequisites
This project uses `uv` for dependency management.

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   uv sync
   ```

### Running the Project
The core logic and analysis are contained within the Jupyter notebook:
```bash
jupyter lab 24f2004142-notebook-t12026.ipynb
```

## ✍️ Author

**Varun Agnihotri (@PythonicVarun)**
- [GitHub](https://github.com/PythonicVarun)
- [Kaggle](https://kaggle.com/PythonicVarun)
