import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="romjan",
    database="school"
)

query = "CREATE DATABASE IF NOT EXISTS school"
cursor = connection.cursor()

cursor.execute(query)

def create_table(tablename):
    query = f"""
                CREATE TABLE IF NOT EXISTS {tablename}(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    age INT,
                    grade FLOAT
                )
            """
    cursor = connection.cursor()
    cursor.execute(query)

def add_student(name, age, grade):
    query = """
                INSERT INTO students(name, age, grade)
                VALUES(%s, %s, %s)
            """
    cursor = connection.cursor()
    cursor.execute(query, (name, age, grade))
    
    connection.commit()

def update_grade(id, grade):
    query = """
                UPDATE students
                SET grade = %s
                WHERE id = %s
            """
    cursor = connection.cursor()
    cursor.execute(query, (grade, id))
    
    connection.commit()

def increase_age(id, val):
    query = "SELECT age FROM students WHERE ID = %s"
    cursor = connection.cursor()
    cursor.execute(query, (id))
    
    age = cursor.fetchone()
    newage = age[0] + val
    
    cursor.execute("""
                    UPDATE students
                    SET age = %s
                    WHERE id = %s
                   """, (newage, id))
    
    connection.commit()

def view_all_students():
    query = "SELECT * FROM students"
    cursor = connection.cursor()
    cursor.execute(query)
    students = cursor.fetchall()
    
    for student in students:
        print(f"""
                id = {student[0]}
                name = {student[1]}
                age = {student[2]}
                grade = {student[3]}
              """)

while True:
    print("""
            1. Create Table
            2. Add Student
            3. Update Grade
            4. Increase Age
            5. View All Student
            0. Exit
          """)
    option = int(input("Enter option: "))
    
    if(option == 1):
        tablename = input("Enter table name: ")
        create_table(tablename)
    elif(option == 2):
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        grade = float(input("Enter grade: "))
        add_student(name, age, grade)
    elif(option == 3):
        id = int(input("Enter id: "))
        grade = float(input("Enter new grade: "))
        update_grade(id, grade)
    elif(option == 4):
        id = int(input("Enter id: "))
        val = int(input("Enter number of age you want to increase: "))
        increase_age(id, val)
    elif(option == 5):
        view_all_students()
    elif(option == 0):
        break
    else:
        print("Wrong option selected")