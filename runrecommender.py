import turicreate as tc 
import sqlite3 as sql 
import pandas as pd

connection = sql.connect('db.sqlite3')
tasteprofile = tc.SFrame.from_sql(connection, "Select user_id, pid_id, status, timestamp from TxnHistory")
connection.close()

m1 = tc.load_model('recommendermodel')
results = m1.recommend()

connection = sql.connect('db.sqlite3')

cursor = connection.cursor()
truncatestatement = "delete from Recommendations"
cursor.execute(truncatestatement)
connection.commit()
emptyframe = pd.DataFrame(columns = ['id'])
resultset = results.to_dataframe()
final_results = pd.concat([emptyframe, resultset], axis = 1)
final_results = final_results[['id','user','pid', 'score', 'rank']]
final_results.to_sql('Recommendations',con = connection, if_exists = 'append', index = False)
connection.commit()
connection.close()