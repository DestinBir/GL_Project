# connection à la bd mysql
from functions import *

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
    inscrire_ajouter_etudiant(connection, '147895678', 'Biringanine', 'Delphin', 'G', 'Bukavu', '1995-06-15', 1, '2024-2025', 'Semestre 1')
    # verifier_etudiant_inscrit(connection, '147895678', 'Semestre 1')
    print('=======================================')