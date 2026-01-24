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
