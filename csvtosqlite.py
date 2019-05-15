import pandas as pd
import sqlite3 as sql

connection = sql.connect('db.sqlite3')
dataset = pd.read_csv('./product_details.csv')
dataset.to_sql('Products',con = connection, if_exists = 'append', index = False)
connection.close()