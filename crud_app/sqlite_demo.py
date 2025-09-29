# it is optional ,it is just to show all data in lust form from database test.db
#iska crud _api create se koi lena dena nhi hain 
import sqlite3

conn=sqlite3.connect('test.db')
cursor=conn.cursor()

#list all the tables in database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables=cursor.fetchall()
print("Tables:",tables)

#Quey from yhe first table
if tables:
    table_name=tables[0][0]
    cursor.execute(f"SELECT * FROM {table_name} ;")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
conn.close()