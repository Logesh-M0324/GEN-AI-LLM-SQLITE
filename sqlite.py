import sqlite3

#connect to sqlite database

connection = sqlite3.connect('student.db')

#create a cursor object to insert tables , create tables

cursor = connection.cursor()


table_info = """ 

CREATE TABLE IF NOT EXISTS STUDENT (Name Varchar(20), class varchar(20), section varchar(5));

"""

cursor.execute(table_info)


cursor.execute("INSERT INTO STUDENT VALUES ('John Doe', '10th Grade', 'A');")
cursor.execute("INSERT INTO STUDENT VALUES ('Jane Smith', '9th Grade', 'B');")
cursor.execute("INSERT INTO STUDENT VALUES ('Emily Davis', '11th Grade', 'C');")
cursor.execute("INSERT INTO STUDENT VALUES ('Michael Brown', '12th Grade', 'A');")
cursor.execute("INSERT INTO STUDENT VALUES ('Sarah Wilson', '10th Grade', 'B');")


print("Data in students table:")

data = cursor.execute("SELECT * FROM STUDENT;")

for row in data:
    print(row)


