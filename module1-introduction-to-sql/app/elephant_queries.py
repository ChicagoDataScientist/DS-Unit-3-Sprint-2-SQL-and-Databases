import psycopg2

# DB_HOST= 'drona.db.elephantsql.com'
# DB_USER='hwdutxsg'
# DB_NAME='hwdutxsg'
# DB_PASSWORD='9sr1DjHLpye6vnBVoFCGYpgGmbjblc_S'



import os
from dotenv import load_dotenv
import psycopg2

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print (type(conn))
cur = conn.cursor()

print (type(cur))


query = 'SELECT * from test_table;'
cur.execute(query)

# cur.execute(query)
# results = cur.fetchone()
# print(type(results))
# print(results)

cur.execute(query)
results = cur.fetchall()
print(type(results))
print(results)