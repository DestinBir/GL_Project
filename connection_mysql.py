# connection à la bd mysql

import mysql.connector

with mysql.connector.connect(
    host="localhost",  
    user="root",
    password="root",
    database="GestNotes"
) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM etudiant")
    print('It works')