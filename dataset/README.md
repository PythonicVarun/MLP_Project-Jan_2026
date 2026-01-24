# Dataset Description

### Data Files

The dataset consists of the following files:

- **train.csv:** The training set, including the target variable label along with all feature columns.
- **test.csv:** The test set, containing the same feature columns but excluding the target variable label.
- **sample_submission.csv:** A sample submission file provided in the correct format for competition submissions.

### Columns Description

- **comment**: The raw text content of the comment.
- **created_date**: The date and time when the comment was posted.
- **post_id**: A unique identifier linking the comment to a discussion thread or parent post.
- **emoticon_1**: Indicator for the presence of symbols from the first internal emoticon group.
- **emoticon_2**: Indicator for the presence of symbols from the second internal emoticon group.
- **emoticon_3**: Indicator for the presence of symbols from the third internal emoticon group.
- **upvote**: Number of positive reactions received by the comment.
- **downvote**: Number of negative reactions received by the comment.
- **if_1**: Internal feature one that is hidden by the platform.
- **if_2**: Internal feature two that is hidden by the platform.
- **race**: Indicator showing whether the system detected references to a specific group identity.
- **religion**: Indicator showing whether the system detected references to a belief-related topic.
- **gender**: Indicator showing whether the system detected references to a gender-related topic.
- **disability**: Indicator showing whether the system detected references to an ability-related topic.
- **label**: The final category assigned to the comment by the platform (Target Variable). This variable can take four distinct - values, each corresponding to a different internal handling category.
