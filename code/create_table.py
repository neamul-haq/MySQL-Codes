import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql_command = """
                CREATE TABLE Student(
                    roll INT,
                    first_name VARCHAR(20),
                    last_name VARCHAR(20)
                );  
              """
              
mycursor.execute(sql_command)