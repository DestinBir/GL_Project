# connection à la bd mysql
from functions import *
from read_xlsx import *

import mysql.connector

with mysql.connector.connect(
    host="localhost",  
    user="root",
    password="",
    database="GestNotes"
) as connection:
    print('=======================================')
    print('Connexion réussie à la base de données.')
    print('=======================================')
    print('')
    print('=======================================')
    # inscrire_ajouter_etudiant(connection, '165895678', 'Baraka', 'Elie', 'M', 'Bukavu', '1995-06-15', 1, '2024-2025', 'Semestre 1')
    # verifier_etudiant_inscrit(connection, '147895678', 'Semestre 1')
    # print(get_etudiant_by_promotion_per_semester(connection, 1, 'Semestre 1'))
    # print(get_etudiant(connection, '147895623'))
    # inscrire_from_excel version 2
    # insert_promotion('BAC 3 Génie Logiciel', connection)
    # insert_promotion('BAC 3 Systèmes Informatiques', connection)
    # inscrire_etudiant_depuis_excel("format.xlsx", connection, 1, "2024-2025", "Semestre 1")
    # insert_etudiant_list_of_tuples(connection.cursor(), get_data_from_excel("format.xlsx"))
    print(get_promotions(connection))
    print('=======================================')