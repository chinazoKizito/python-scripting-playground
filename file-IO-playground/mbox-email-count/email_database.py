import sqlite3

connection = sqlite3.connect('emaildb.sqlite')
cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS Counts""")
cursor.execute("""CREATE TABLE Counts ( email TEXT UNIQUE, counts INTEGER)""")

emails = []
fhand = open("./mbox.txt")
print("Connected to mbox.txt")

for line in fhand:
    line.rstrip()
    if line.startswith("From"):
        line = line.split(' ')
        line1 = (line[1].strip('\n'))
        emails.append(line1)

print(emails)
for email in emails:
    cursor.execute("""SELECT counts FROM Counts WHERE email = ?""", (email,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute("""INSERT INTO Counts (email, counts) VALUES (?, 1)""", (email,))
    else:
        cursor.execute("""UPDATE Counts SET counts = counts + 1 WHERE email = ?""", (email,))
    connection.commit()

descending_email = "SELECT email, counts FROM Counts ORDER BY counts DESC LIMIT 10"
for row in cursor.execute(descending_email):
    print(str(row[0]), row[1])

cursor.close()
