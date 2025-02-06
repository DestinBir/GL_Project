# connection à la bd mysql
from .functions import insert_or_update_etudiant, insert_promotion, insert_or_update_inscription
import mysql.connector

with mysql.connector.connect(
    host="localhost",  
    user="root",
    password="",
    database="GestNotes"
) as connexion:
    insert_promotion('Bac3 Informatique', c)