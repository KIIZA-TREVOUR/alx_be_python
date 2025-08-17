import mysql.connector
from mysql.connector import Error

# Define globals
connection = None
cursor = None

def connect_to_database():
    global connection, cursor  # declare that we’re using the globals
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Trevour256!',
            database='school',
            port=3308
        )
        if connection.is_connected():
            cursor = connection.cursor()
            print("Successfully connected to MySQL")
    except Error as e:
        print(f"Error: {e}")

def add_student(name, age, email):
    global connection, cursor  # declare that we’re using the globals
    try:
        sql = "INSERT INTO students(name, age, email) VALUES (%s, %s, %s)"
        values = (name, age, email)
        cursor.execute(sql, values)
        connection.commit()
        print(f"Student {name} added successfully!")
        print(f"Record ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Error: {e}")
        # -------------------------------
# Fetch all students
# -------------------------------
def get_all_students():
    global connection, cursor 
    try:
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()
        print("Total students:", cursor.rowcount)
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}")
    except Error as e:
        print(f"Error: {e}")


# -------------------------------
# Search students by age
# -------------------------------
def get_students_above_age(age):
    global connection, cursor 
    try:
        cursor.execute("SELECT * FROM students WHERE age > %s", (age,))
        records = cursor.fetchall()
        print(f"Students older than {age}:")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}")
    except Error as e:
        print(f"Error: {e}")


# -------------------------------
# Update student information
# -------------------------------
def update_student_age(student_id, new_age):
    global connection, cursor 
    try:
        sql = "UPDATE students SET age = %s WHERE id = %s"
        values = (new_age, student_id)
        cursor.execute(sql, values)
        connection.commit()
        if cursor.rowcount > 0:
            print(f"Student updated successfully! Rows affected: {cursor.rowcount}")
        else:
            print("No student found with that ID")
    except Error as e:
        print(f"Error: {e}")


# -------------------------------
# Delete student by ID
# -------------------------------
def delete_student(student_id):
    global connection, cursor 
    try:
        # Check if student exists
        cursor.execute("SELECT name FROM students WHERE id = %s", (student_id,))
        student = cursor.fetchone()
        if student:
            sql = "DELETE FROM students WHERE id = %s"
            cursor.execute(sql, (student_id,))
            connection.commit()
            print(f"Student '{student[0]}' deleted successfully!")
        else:
            print("Student not found")
    except Error as e:
        print(f"Error: {e}")


# -------------------------------
# Get students with their enrolled courses
# -------------------------------
def get_student_enrollments():
    global connection, cursor 
    try:
        sql = """
        SELECT s.name AS student_name, c.title AS course_title, e.grade
        FROM students s
        INNER JOIN enrollments e ON s.id = e.student_id
        INNER JOIN courses c ON e.course_id = c.id
        ORDER BY s.name
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(f"{row[0]} is enrolled in {row[1]} (Grade: {row[2]})")
    except Error as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    connect_to_database()
    if connection and cursor:
        # add_student("Janet", 12, "email3@gmail.com")
        
        # # Fetch all students

        # # Get students above age 18
        # get_students_above_age(18)

        # # Update student age
        # update_student_age(8, 18)

        # Delete student
        # delete_student(4)
        # get_all_students()

        # Show student enrollments
        get_student_enrollments()
        # Close after done
        cursor.close()
        connection.close()
