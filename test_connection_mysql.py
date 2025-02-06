# connection à la bd mysql
from functions import *

import mysql.connector

with mysql.connector.connect(
    host="localhost",  
    user="root",
    password="",
    database="GestNotes"
) as connection:
    inscrire(connection, '147895623', 'Biringanine', 'Destin', 'M', 'Bukavu', '1995-06-15', 1, '2024-2025', 'Semestre 1')