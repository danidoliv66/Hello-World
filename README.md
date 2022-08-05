# Hello-World
My first repository for testing purpose.
I'm going to add some code here for later updatings.

# These  codes are working:
- Using TextVectorization layer
- Stop words removal from handmade file
- Embedding from word2vec (I should explore fasttext and TF embeddings)
- Using 300 vector dimension (I should use more dimensions)
- Using class weights

# Parameters:
- max_seq_len = 300
- vector_size = 5000    # I should increase this value
- window_size = 2
- w2v_epochs  = 10     # this value works very well
- min_delta   = 0.01
- BATCH_SIZE  = 128    # more than this gives error for memory usage!
- patience    = 10
- NN_epochs   = 60
- verbose     = 0
- vocab_size  = 22113

## Classification:
- loss_func   = 'categorical_crossentropy'
- metric      = ['AUC']

## Regression:
- loss_func   = 'mean_squared_error'
- metric      = ['mse']

# Results:
## Overall metrics

| Metrics | Classification | Regression |
| :--- | :---: | :---: |
| Overall ACC | 59.5 | 59.7 |
| ACC Macro | 83.8 | 83.9 |
| F1-Macro | 56.2 | 56.9 |
| TPR Macro (recall) | 0.61 | 0.60 |
| TPR Micro (recall) | 0.59 | 0.60 |
| TNR Macro | 0.89 | 0.89 |
| TNR Micro | 0.90 | 0.90 |


## Per class metrics
### (classification)
| Metrics | 1 | 2 | 3 | 4 | 5 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Accuracy | 95.5 | 92.5 | 81.4 | 68.7 | 80.7 |
| F1-score | 62.1 | 38.3 | 54.7 | 60.4 | 65.7 |
| AUC | 88.1 | 70.8 | 71.2 | 67.1 | 77.1 |
| AUCI | Very Good | Good | Good | Fair | Good |

### (regression)
| Metrics | 1 | 2 | 3 | 4 | 5 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Accuracy | 97.1 | 92.1 | 80.9 | 68.4 | 80.8 |
| F1-score | 97.1 | 92.1 | 80.9 | 68.4 | 80.8 |
| AUC | 82.6 | 75.7 | 69.8 | 67.3 | 76.3 |
| AUCI | Very Good | Good | Fair | Fair | Good |

# Next steps:
Next steps are done in Daniel/TextVectorization, using Refression model `PT_Reg_Ratings_solid_ImBalanced.py`.
