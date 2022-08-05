# Hello-World
My first repository for testing purpose.
I'm going to add some code here for later updatings.

# These  codes are working:
- Using TextVectorization layer
- Stop words removal from handmade file
- Embedding from word2vec (I should explore fasttext and TF embeddings)
- Using 300 vector dimension (I should use more dimensions)
- Using class weights

# Results:

## Classification of ratings with cost sensitive weights (`PT_Class_Ratings_solid_ImBalanced.py`):
### Parameters:
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

- loss_func   = 'categorical_crossentropy'
- metric      = ['AUC']

| Overall metrics |
| Metrics | Classification | Regression |
| :--- | :---: | :---: |
| Overall ACC | 59.5 |  |
| ACC Macro | 83.8 |  |
| F1-Macro | 56.2 |  |
| TPR Macro (recall) | 0.61 |  |
| TPR Micro (recall) | 0.59 |  |
| TNR Macro | 0.89 |  |
| TNR Micro | 0.90 |  |


| Per class metrics |
| Metric | Accuracy<td colspan=2> | F1-score | AUC |
|  | Class | Reg | Class | Reg | Class | Reg |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |

