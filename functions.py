import mysql.connector
from mysql.connector import Error

def insert_or_update_etudiant(cursor, matricule, nom, prenom, sexe, lieu_naissance, date_naissance):
    # Insérer ou mettre à jour un étudiant dans la table Etudiant
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


# Exemple d'utilisation
# inserer_promotion('Promotion 2024')


def insert_inscription(cursor, matricule, id_promo, année_académique, semestre):
    # Insérer ou mettre à jour une inscription dans la table Inscrire
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

def verifier_etudiant_exist(conn, matricule):
    cursor = conn.cursor()
    
    sql = "SELECT * FROM Etudiant WHERE matricule = %s"
    
    cursor.execute(sql, (matricule,))

    etudiants = cursor.fetchall()
    
    if etudiants:
        print("Cet etudiant existe déjà !")
        return True
    else:
        print("Cet etudiant n'existe pas !")
        return False

def verifier_etudiant_inscrit(conn, matricule, semestre):
    cursor = conn.cursor()
    
    sql = "SELECT * FROM Inscrire WHERE matricule = %s AND Semestre = %s"
    
    cursor.execute(sql, (matricule, semestre))

    etudiants = cursor.fetchall()
    
    if etudiants:
        print("Cet étudiant est inscrit !")
        return True
    else:
        print("Cet étudiant n'est pas inscrit !")
        return False


def inscrire(conn, matricule, nom, prenom, sexe, lieu_naissance, date_naissance, id_promo, année_académique, semestre):
    cursor = conn.cursor()

    if insert_or_update_etudiant(cursor, matricule, nom, prenom, sexe, lieu_naissance, date_naissance):
        print("Étudiant inséré ou mis à jour avec succès.")
    
    if insert_or_update_inscription(cursor, matricule, id_promo, année_académique, semestre):
        print("Inscription ajoutée ou mise à jour avec succès.")
        
    print('Tout a été fait !')
    


    conn.commit()
    cursor.close()
    conn.close()
