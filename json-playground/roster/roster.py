import json
import sqlite3

connection = sqlite3.connect('rosterdb.sqlite')
cursor = connection.cursor()

# setup
cursor.executescript("""
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course; 

CREATE TABLE User( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Course( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE);
CREATE TABLE Member(user_id INTEGER, course_id INTEGER, role Integer, PRIMARY KEY(user_id, course_id));
"""
                     )

fname = input('Enter File name possibly Json: ')
if len(fname) < 1:
    fname = './roster_data_sample.json'

print('working  with  "roster_data_sample.json"')
data = open(fname).read()
json_data = json.loads(data)

for entry in json_data:
    name = entry[0]
    course = entry[1]
    role = entry[2]

    cursor.execute("""
    INSERT OR IGNORE INTO User (name) VALUES (?)""", (name,))
    cursor.execute("""
    SELECT id FROM User WHERE name = ?""", (name,))
    user_id = cursor.fetchone()[0]

    cursor.execute("""
    INSERT OR IGNORE INTO Course (title) VALUES (?)""", (course,))
    cursor.execute("""
    SELECT id FROM Course where title = ?""", (course,))
    course_id = cursor.fetchone()[0]

    cursor.execute("""
    INSERT OR REPLACE INTO MEMBER (user_id, course_id, role) VALUES (?, ?, ?)""", (user_id, course_id, role))

    connection.commit()

print('Work Done Boss')
