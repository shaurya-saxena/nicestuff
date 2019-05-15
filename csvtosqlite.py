import pandas as pd

dataset = pd.read_csv('./product_details.csv')

for row in dataset:
    print(row)
