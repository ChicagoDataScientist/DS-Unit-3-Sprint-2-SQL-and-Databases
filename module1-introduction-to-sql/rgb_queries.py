import sqlite3
DB_FILEPATH = 'rpg_db.sqlite3'
connection = sqlite3.connect('rpg_db.sqlite3')
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query1 = """
SELECT count (*)
from charactercreator_character
"""
result1 = cursor.execute(query1).fetchall()
print("RESULT 1", result1)