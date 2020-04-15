import sqlite3
import pandas as pd
df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
df.to_sql('users', con=conn)
# conn.row_factory = sqlite3.Row
print ("hello world")