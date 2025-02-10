import mysql.connector
from mysql.connector import Error
from read_xlsx import *

import datetime


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
                INSERT INTO Etudiant (matricule, NomsEtu, PrenomEtu, Sexe, LieuNais, DateNais)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    NomsEtu = VALUES(NomsEtu),
                    PrenomEtu = VALUES(PrenomEtu),
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
    """
    Insère une liste de tuples d'étudiants dans la base de données.
    """
    print(etudiants)
    try:
        cursor.executemany("""
            INSERT INTO Etudiant (matricule, NomsEtu, PrenomEtu, Sexe, LieuNais, DateNais)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                NomsEtu = VALUES(NomsEtu),
                PrenomEtu = VALUES(PrenomEtu),
                Sexe = VALUES(Sexe),
                LieuNais = VALUES(LieuNais),
                DateNais = VALUES(DateNais)
        """, etudiants)
        print('Everything okay !')
    except Error as e:
        print(f"Erreur lors de l'insertion ou de la mise à jour des étudiants : {e}")
        return False
    return True

def update_etudiant(cursor, matricule, nom, prenom, sexe, lieu_naissance, date_naissance):
    
    try:
        cursor.execute("""
            INSERT INTO Etudiant (matricule, NomsEtu, PrenomEtu, Sexe, LieuNais, DateNais)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                NomsEtu = VALUES(NomsEtu),
                PrenomEtu = VALUES(PrenomEtu),
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
                INSERT INTO Inscrire (matricule, id_promo, AnneeAcademique, Semestre)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    AnneeAcademique = VALUES(AnneeAcademique),
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
        # SQL query to get student matricules based on promotion and semester
        sql = """
        SELECT E.matricule, E.NomsEtu, E.PrenomEtu, E.Sexe, E.LieuNais, E.DateNais
        FROM Etudiant E
        JOIN Inscrire I ON E.matricule = I.matricule
        WHERE I.id_promo = %s AND I.Semestre = %s
        """
        cursor.execute(sql, (promotion, semestre))
        etudiant_data = cursor.fetchall()
        
        # Process each student and append their data in the required format
        for etudiant in etudiant_data:
            etudiants.append((
                etudiant[0],  # matricule
                etudiant[1],  # NomEtu
                etudiant[2],  # PrenomEtu
                etudiant[3],  # Sexe
                etudiant[4],  # LieuNais
                etudiant[5]   # DateNais (should be a datetime object)
            ))
        
        return etudiants
    except Error as e:
        print(f"Erreur lors de la récupération des étudiants de la promotion : {e}")
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
        
        # Vérifier si l'étudiant existe déjà
        cursor.execute("SELECT COUNT(*) FROM Etudiant WHERE matricule = %s", (matricule,))
        etudiant_existe = cursor.fetchone()[0] > 0
        
        if not etudiant_existe:
            try:
                cursor.execute("""
                    INSERT INTO Etudiant (matricule, NomsEtu, PrenomEtu, Sexe, LieuNais, DateNais)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        NomsEtu = VALUES(NomsEtu),
                        PrenomEtu = VALUES(PrenomEtu),
                        Sexe = VALUES(Sexe),
                        LieuNais = VALUES(LieuNais),
                        DateNais = VALUES(DateNais)
                """, (matricule, nom, prenom, sexe, lieu_naissance, date_naissance))
                print(f"Étudiant {matricule} ajouté avec succès.")
            except Error as e:
                print(f"Erreur lors de l'insertion de l'étudiant {matricule} : {e}")
                continue
        else:
            print(f"L'étudiant {matricule} existe déjà.")
        
        # Vérifier si l'étudiant est déjà inscrit à ce semestre
        cursor.execute("""
            SELECT COUNT(*) FROM Inscrire WHERE matricule = %s AND Semestre = %s
        """, (matricule, semestre))
        inscription_existe = cursor.fetchone()[0] > 0
        
        if not inscription_existe:
            try:
                cursor.execute("""
                    INSERT INTO Inscrire (matricule, id_promo, AnneeAcademique, Semestre)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        AnneeAcademique = VALUES(AnneeAcademique),
                        Semestre = VALUES(Semestre)
                """, (matricule, id_promo, annee_academique, semestre))
                print(f"Inscription de l'étudiant {matricule} ajoutée avec succès.")
            except Error as e:
                print(f"Erreur lors de l'inscription de l'étudiant {matricule} : {e}")
                
        else:
            print(f"L'étudiant {matricule} est déjà inscrit à ce semestre.")
    
        conn.commit()
    cursor.close()
    print('=======================================')
    print('Inscription réussie à la base de données.')
    print('=======================================')
    conn.close()
    
    return True

def authentification_appariteur():
    pass

def get_promotions(conn):
    cursor = conn.cursor()
    
    try:
        sql = "SELECT * FROM Promotion "
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as e:
        print(f"Erreur lors de la recupération des etudiants de la promotion : {e}")