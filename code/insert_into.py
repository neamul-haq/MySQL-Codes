import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql_command = """
                INSERT INTO Student(roll, first_name, last_name)
                VALUES(2, "kalam", "Mridha"); 
              """
              
mycursor.execute(sql_command)
mydb.commit()