import turicreate as tc 
import sqlite3 as sql 

connection = sql.connect('db.sqlite3')

tasteprofile = tc.SFrame.from_sql(connection, "Select user_id, pid_id, status, timestamp from TxnHistory")
connection.close()

m1 = tc.load_model('recommendermodel')

results = m1.recommend()
#results.export_csv('recommendations.csv')

connection = sql.connect('db.sqlite3')
for row in results:
    connection.execute('INSERT INTO Recommendations(user, pid, score, rank) VALUES(results[1], results[2], results[3], results[4])',var)

connection.close()