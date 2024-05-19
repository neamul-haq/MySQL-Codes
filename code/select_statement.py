import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "hr"
)

mycursor = mydb.cursor()

sql_command = """
                SELECT *
                FROM employees;  
              """
              
mycursor.execute(sql_command)

data = mycursor.fetchall()

for i in data:
    print(i)