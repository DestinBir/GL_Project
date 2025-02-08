import mysql.connector
from mysql.connector import Error
from read_xlsx import *


def verifier_etudiant_exist(cursor, matricule):
    sql = "SELECT * FROM Etudiant WHERE matricule = %s"
    
    cursor.execute(sql, (matricule,))

    etudiants = cursor.fetchall()
    
    if etudiants:
        
        return True
    else:
        
        return False


def verifier_etudiant_inscrit(cursor, matricule, semestre):
    sql = "SELECT * FROM Inscrire WHERE matricule = %s AND Semestre = %s"
    
    cursor.execute(sql, (matricule, semestre))

    etudiants = cursor.fetchall()
    
    if etudiants:
        
        return True
    else:
        
        return False


def insert_etudiant(cursor, matricule, nom, prenom, sexe, lieu_naissance, date_naissance):
    
    test = verifier_etudiant_exist(cursor, matricule)
    
    if not test:
        try:
            cursor.execute("""
                INSERT INTO Etudiant (matricule, NomsEtu, PrénomEtu, Sexe, LieuNais, DateNais)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    NomsEtu = VALUES(NomsEtu),
                    PrénomEtu = VALUES(PrénomEtu),
                    Sexe = VALUES(Sexe),
                    LieuNais = VALUES(LieuNais),
                    DateNais = VALUES(DateNais)
            """, (matricule, nom, prenom, sexe, lieu_naissance, date_naissance))
        except Error as e:
            print(f"Erreur lors de l'insertion ou de la mise à jour de l'étudiant : {e}")
            return False
        return True
    else:
        print(f"Erreur lors de l'ajout de l'étudiant car il existe déjà")
        return False 

def insert_etudiant_list_of_tuples(cursor, etudiants):

def update_etudiant(cursor, matricule, nom, prenom, sexe, lieu_naissance, date_naissance):
    
    try:
        cursor.execute("""
            INSERT INTO Etudiant (matricule, NomsEtu, PrénomEtu, Sexe, LieuNais, DateNais)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                NomsEtu = VALUES(NomsEtu),
                PrénomEtu = VALUES(PrénomEtu),
                Sexe = VALUES(Sexe),
                LieuNais = VALUES(LieuNais),
                DateNais = VALUES(DateNais)
        """, (matricule, nom, prenom, sexe, lieu_naissance, date_naissance))
    except Error as e:
        print(f"Erreur lors de l'insertion ou de la mise à jour de l'étudiant : {e}")
        return False
    return True


def insert_promotion(desi_promo, conn):
        
        # Requête SQL pour insérer ou mettre à jour la promotion
        query = """
        INSERT INTO Promotion (DesiPromo)
        VALUES (%s)
        ON DUPLICATE KEY UPDATE
            DesiPromo = VALUES(DesiPromo);
        """
        
        params = (desi_promo,)
        
        cursor = conn.cursor()
        cursor.execute(query, params)
        
        
        conn.commit()
        print("Promotion ajoutée ou mise à jour avec succès.")


def insert_inscription(cursor, matricule, id_promo, année_académique, semestre):

    test = verifier_etudiant_inscrit(cursor, matricule, semestre)
    if not test:
        try:
            cursor.execute("""
                INSERT INTO Inscrire (matricule, id_promo, AnnéeAcadémique, Semestre)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    AnnéeAcadémique = VALUES(AnnéeAcadémique),
                    Semestre = VALUES(Semestre)
            """, (matricule, id_promo, année_académique, semestre))
        except Error as e:
            print(f"Erreur lors de l'insertion ou de la mise à jour de l'inscription : {e}")
            return False
        return True
    else:
        print(f"Erreur lors de l'ajout de l'inscription car l'étudiant est déjà inscrit à ce semestre")
        return False 


def connect_to_db():
    # Connexion à la base de données MySQL
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='',  
            database='GestNotes'
        )
        if conn.is_connected():
            print('Connexion réussie à la base de données.')
            return conn
    except Error as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None


def inscrire_ajouter_etudiant(conn, matricule, nom, prenom, sexe, lieu_naissance, date_naissance, id_promo, année_académique, semestre):
    cursor = conn.cursor()

    if insert_etudiant(cursor, matricule, nom, prenom, sexe, lieu_naissance, date_naissance):
        print("Étudiant ajouté avec succès.")
    
        if insert_inscription(cursor, matricule, id_promo, année_académique, semestre):
            print("Inscription ajoutée avec succès.")
        
        print('Good 😂😂🎉')
    else:
        print('Bad 😂😂🎉')
    
    cursor.close()
    conn.commit() 
    
    
def get_etudiant(conn, matricule):
    cursor = conn.cursor()
    
    try:
        sql = "SELECT * FROM Etudiant WHERE matricule = %s "
        cursor.execute(sql, (matricule,))
        return cursor.fetchall()
    except Error as e:
        print(f"Erreur lors de la recupération des etudiants de la promotion : {e}")
        

def get_etudiant_by_promotion_per_semester(conn, promotion, semestre):
    
    cursor = conn.cursor()
    etudiants = []
    
    try:
        sql = "SELECT * FROM Inscrire WHERE id_promo = %s AND Semestre = %s"
        cursor.execute(sql, (promotion, semestre))
        inscriptions = cursor.fetchall()
        
        for inscription in inscriptions:
            etudiants.append(get_etudiant(conn, inscription[1]))
        
        return etudiants
    except Error as e:
        print(f"Erreur lors de la recupération des etudiants de la promotion : {e}")
        
        return etudiants
    
    
def get_etudiant_by_promotion(conn, promotion):
    
    cursor = conn.cursor()
    etudiants = []
    
    try:
        sql = "SELECT * FROM Inscrire WHERE id_promo = %s"
        cursor.execute(sql, (promotion,))
        inscriptions = cursor.fetchall()
        
        for inscription in inscriptions:
            etudiants.append(get_etudiant(conn, inscription[1]))
        
        return etudiants
    except Error as e:
        print(f"Erreur lors de la recupération des etudiants de la promotion : {e}")
        
        return etudiants
    

def inscrire_etudiant_depuis_excel(path, conn, id_promo, annee_academique, semestre):
    """
    Insère les étudiants et leurs inscriptions à partir d'un fichier Excel.
    """
    data = get_data_from_excel(path)

    for item in data:
        cursor = conn.cursor()
        matricule = item["matricule"]
        nom = item["nom"]
        prenom = item["prenom"]
        sexe = item["sexe"]
        lieu_naissance = item["lieunais"]
        date_naissance = item["datenais"]
        
        print(matricule)

        insert_etudiant(cursor, matricule, nom, prenom, sexe, lieu_naissance, date_naissance)
        
        conn.commit()
        cursor.close()
    print('=======================================')
    print('Inscription réussie à la base de données.')
    print('=======================================')
    conn.close()

