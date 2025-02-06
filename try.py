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
            user='root',  # Remplacez par votre utilisateur
            password='',  # Remplacez par votre mot de passe
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

    # Exemple d'ajout ou de mise à jour d'un étudiant
    matricule = '1234567890'
    nom = 'Doe'
    prenom = 'John'
    sexe = 'M'
    lieu_naissance = 'Paris'
    date_naissance = '1995-06-15'
    
    if insert_or_update_etudiant(cursor, matricule, nom, prenom, sexe, lieu_naissance, date_naissance):
        print("Étudiant inséré ou mis à jour avec succès.")
    
    # Exemple d'ajout ou de mise à jour d'une inscription
    id_promo = 1  # Supposons que l'ID de la promotion soit 1
    année_académique = '2025-2026'
    semestre = 'Semestre 1'

    if insert_or_update_inscription(cursor, matricule, id_promo, année_académique, semestre):
        print("Inscription ajoutée ou mise à jour avec succès.")

    # Commit des changements et fermeture de la connexion
    conn.commit()
    cursor.close()
    conn.close()

"""
if __name__ == '__try__':
    main()
"""