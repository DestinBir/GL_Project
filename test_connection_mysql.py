# connection à la bd mysql
from .try import insert_or_update_etudiant, inserer_promotion, insert_or_update_inscription
import mysql.connector

with mysql.connector.connect(
    host="localhost",  
    user="root",
    password="",
    database="GestNotes"
) as connexion:
    