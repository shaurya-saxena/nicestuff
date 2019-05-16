import turicreate as tc 
import sqlite3 as sql 
import pandas as pd

connection = sql.connect('db.sqlite3')

tasteprofile = tc.SFrame.from_sql(connection, "Select user_id, pid_id, status, timestamp from TxnHistory")
connection.close()

m1 = tc.load_model('recommendermodel')

results = m1.recommend()
#results.export_csv('recommendations.csv')

connection = sql.connect('db.sqlite3')

emptyframe = pd.DataFrame(columns = ['id'])
emptysframe = graphlab.SFrame(emptyframe)
final_results = pd.concat([emptyframe, results], axis = 1)


print(final_results)
#final_results.to_sql(connection, 'Recommendations', "Insert")

#connection.close()