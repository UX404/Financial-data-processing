# Financial-data-processing
Python files to process finantial data.

## 20210605 Data Processing
Process Data to fit the date order.
Add an additional precise feature generated from the original data.

## 20210617 Random Forest / Rearrange Files
Analyzing the data, there's a obvious problem of data imbalance, with 59881 false data and 446 true data.

Thus, the entire dataset is processed in this way:

First, copy false data until it's almost the same amount as true data. Merge them and shuffle.

Then, classify them using random forest.

Usually random forest is run like 100 times on the whole dataset.

However, in this situation, for every random tree we randomly pick 1000 data, which uniformly picks basically all the true data and a part of false data.

Data are run on 100-10000 random trees, whose results are given as follows:

| Sample Nums / Tree Nums | Train Acc. | Test Acc. | Percision | Recall | F1-Score | Time |
|          ----           |    ----    |    ----   |   ----    |  ----  |   ----   | ---- |
| 1000 / 100 | 98.83% | 77.90% | 0.82 | 0.78 |  0.77 | 0.97s |
| 1000 / 500 | 98.87% | 78.05% | 0.83 | 0.78 | 0.77 | 4.87s |
| 1000 / 1000 | 98.91% | 78.04% | 0.83 | 0.78 | 0.77 | 9.00s |
| 5000 / 1000 | 99.74% | 76.02% | 0.82 | 0.76 | 0.75 | 12.72s |
| 10000 / 1000 | 99.87% | 76.09% | 0.82 | 0.76 | 0.75 | 16.92s |
| 1000 / 5000 | 98.90% | 78.07% | 0.83 | 0.78 | 0.77 | 41.45s |
| 1000 / 10000 | 98.90% | 78.04% | 0.83 | 0.78 | 0.77 | 79.54s |
