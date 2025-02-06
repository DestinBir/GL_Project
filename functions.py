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

def inserer_promotion(desi_promo, connection):
        
        # Requête SQL pour insérer ou mettre à jour la promotion
        query = """
        INSERT INTO Promotion (DesiPromo)
        VALUES (%s)
        ON DUPLICATE KEY UPDATE
            DesiPromo = VALUES(DesiPromo);
        """
        
        params = (desi_promo,)
        
        cursor = connection.cursor()
        cursor.execute(query, params)
        
        
        connection.commit()
        print("Promotion ajoutée ou mise à jour avec succès.")


# Exemple d'utilisation
# inserer_promotion('Promotion 2024')


def insert_or_update_inscription(cursor, matricule, id_promo, année_académique, semestre):
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


def main():
    # Connexion à la base de données
    conn = connect_to_db()
    if not conn:
        return

    cursor = conn.cursor()

    
    matricule = '1234567890'
    nom = 'Destin'
    prenom = 'Baseme'
    sexe = 'M'
    lieu_naissance = 'Paris'
    date_naissance = '2000-5-6'
    
    if insert_or_update_etudiant(cursor, matricule, nom, prenom, sexe, lieu_naissance, date_naissance):
        print("Étudiant inséré ou mis à jour avec succès.")
    
    
    id_promo = 1  
    année_académique = '2025-2026'
    semestre = 'Semestre 1'

    if insert_or_update_inscription(cursor, matricule, id_promo, année_académique, semestre):
        print("Inscription ajoutée ou mise à jour avec succès.")

    
    conn.commit()
    cursor.close()
    conn.close()

"""
if __name__ == '__try__':
    main()
"""