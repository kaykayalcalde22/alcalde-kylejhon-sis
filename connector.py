import mysql.connector

class connector:
   db = mysql.connector.connect(
        user="root",
        password="",
        db="student_information_system")
  cursor = db.cursor()   