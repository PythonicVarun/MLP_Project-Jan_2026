# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [[d83af62](https://github.com/PythonicVarun/MLP_Project-Jan_2026/commit/d83af620003acc7d8ddc4fafd1731030e09252d5)] 26-01-2026
- Added conversion of dataset to Sparse Matrices, which significantly reduced the memory usage and [model building time](https://github.com/PythonicVarun/MLP_Project-Jan_2026/blob/89e43e7c51ab040a70c38807493d4639749c684f/24f2004142-notebook-t12026.ipynb?short_path=baf278b#L1402-L1429) from **$\sim$ 30 mins** to **$\sim$ 10 mins**.

## [165a8e3](https://github.com/PythonicVarun/MLP_Project-Jan_2026/commit/165a8e35277bf48fecef2af8a482c86654bda8d5) 08-02-2026
- Added some new features in feature engineering, which improved the model performance by **$\sim$ 1%**.
- Fixed logical errors in text cleaning function, which caused some noise in the data and improved the model performance by **$\sim$ 1%**.

## [7f23d46](https://github.com/PythonicVarun/MLP_Project-Jan_2026/commit/7f23d46be009798d681d8987a951b64a3dd5e50f) 10-02-2026
- Added character level TF-IDF features, which improved the model performance by **$\sim$ 1%**.

## [028b483](https://github.com/PythonicVarun/MLP_Project-Jan_2026/commit/028b483b385ecc4ba88ce93c3f0efe920798773e) 11-02-2026
- Added english stop words in text cleaning function, which improved the model performance by **$\sim$ 0.5%**.
- Increased max features in TF-IDF vectorizer from 2500 to 3000, which improved the model performance by **$\sim$ 0.5%**.
- Added MLP model for ensemble, which improved the model performance by **$\sim$ 1%**.
