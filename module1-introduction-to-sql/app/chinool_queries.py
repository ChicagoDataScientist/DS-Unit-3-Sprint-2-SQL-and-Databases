# app/chinook_queries.py
import sqlite3
import pandas as pd
import os

#DB_FILEPATH = "data/chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "chinook.db")
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row
print(type(conn)) #> <class 'sqlite3.Connection'>


# conn = sqlite3.connect("../data/chinook.db")
# conn.row_factory = sqlite3.Row
# print(type(conn)) #> <class 'sqlite3.Connection'>
curs = conn.cursor()
print(type(curs)) #> <class 'sqlite3.Cursor'>
#query = "SELECT count(distinct CustomerId) as customer_count FROM customers"
# #query = """
# #SELECT count(distinct CustomerId) as customer_count FROM customers
# #"""
query = "SELECT * FROM customers LIMIT 3"
results = curs.execute(query)
print("RESULTS", results)
results2 = curs.execute(query).fetchall()
print("--------")
print("RESULTS 2", results2)
print("----------")
results3 = curs.execute(query).fetchone()
print("RESULTS 3", results3)
print(results3["FirstName"])
breakpoint()
print ("hello world")