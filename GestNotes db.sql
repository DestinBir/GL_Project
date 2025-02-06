CREATE DATABASE GestNotes;
USE GestNotes;

CREATE TABLE Etudiant (
    matricule CHAR(10) PRIMARY KEY,
    NomsEtu VARCHAR(50),
    PrénomEtu VARCHAR(50),
    Sexe CHAR(1),
    LieuNais VARCHAR(50),
    DateNais DATE
) ENGINE=InnoDB;

CREATE TABLE SecJury (
    id_sec INT AUTO_INCREMENT PRIMARY KEY,
    NomsSec VARCHAR(50),
    PrénomSec VARCHAR(50),
    mail VARCHAR(100) UNIQUE
) ENGINE=InnoDB;


CREATE TABLE Promotion (
    id_promo INT AUTO_INCREMENT PRIMARY KEY,
    DesiPromo VARCHAR(50) UNIQUE
) ENGINE=InnoDB;


CREATE TABLE Cours (
    id_cours INT AUTO_INCREMENT PRIMARY KEY,
    DesiCours VARCHAR(50),
    id_promo INT,
    Credit INT,
    FOREIGN KEY (id_promo) REFERENCES Promotion(id_promo) ON DELETE CASCADE
) ENGINE=InnoDB;


CREATE TABLE Inscrire (
    id_inscription INT AUTO_INCREMENT PRIMARY KEY,
    matricule CHAR(10),
    id_promo INT,
    AnnéeAcadémique VARCHAR(9),
    Semestre ENUM('Semestre 1', 'Semestre 2'),
    FOREIGN KEY (matricule) REFERENCES Etudiant(matricule) ,
    FOREIGN KEY (id_promo) REFERENCES Promotion(id_promo) 
) ENGINE=InnoDB;


CREATE TABLE Evaluer (
    id_evaluation INT AUTO_INCREMENT PRIMARY KEY,
    matricule CHAR(10),
    id_cours INT,
    TC FLOAT CHECK (TC BETWEEN 0 AND 10),
    Exam FLOAT CHECK (Exam BETWEEN 0 AND 10),
    FOREIGN KEY (matricule) REFERENCES Etudiant(matricule),
    FOREIGN KEY (id_cours) REFERENCES Cours(id_cours)
) ENGINE=InnoDB;


CREATE TABLE Gérer (
    id_gestion INT AUTO_INCREMENT PRIMARY KEY,
    id_sec INT,
    id_promo INT,
    Semestre ENUM('Semestre 1', 'Semestre 2'),
    FOREIGN KEY (id_sec) REFERENCES SecJury(id_sec),
    FOREIGN KEY (id_promo) REFERENCES Promotion(id_promo)
) ENGINE=InnoDB;
