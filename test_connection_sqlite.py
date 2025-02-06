# pour permettre de faire la connexion avec la BD

import sqlite3

with sqlite3.connect("GestNotes.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM etudiant")
    print('It works')

