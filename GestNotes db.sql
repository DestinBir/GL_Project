CREATE DATABASE GestNotes;
USE GestNotes;

CREATE TABLE Etudiant (
    matricule CHAR(50) PRIMARY KEY,
    NomEtu VARCHAR(50) NOT NULL,
    PrenomEtu VARCHAR(50) NOT NULL,
    Sexe CHAR(1) CHECK (Sexe IN ('M', 'F')),
    LieuNais VARCHAR(50),
    DateNais DATE
) ENGINE=InnoDB;

CREATE TABLE SecJury (
    id_sec INT AUTO_INCREMENT PRIMARY KEY,
    NomSec VARCHAR(50) NOT NULL,
    PrenomSec VARCHAR(50) NOT NULL,
    mail VARCHAR(100) UNIQUE NOT NULL
) ENGINE=InnoDB;

CREATE TABLE Promotion (
    id_promo INT AUTO_INCREMENT PRIMARY KEY,
    DesiPromo VARCHAR(50) UNIQUE NOT NULL
) ENGINE=InnoDB;

CREATE TABLE Cours (
    id_cours INT AUTO_INCREMENT PRIMARY KEY,
    DesiCours VARCHAR(50) NOT NULL,
    id_promo INT,
    Credit INT CHECK (Credit > 0),
    FOREIGN KEY (id_promo) REFERENCES Promotion(id_promo) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE Inscrire (
    id_inscription INT AUTO_INCREMENT PRIMARY KEY,
    matricule CHAR(50),
    id_promo INT,
    AnneeAcademique VARCHAR(9) NOT NULL,
    Semestre ENUM('Semestre 1', 'Semestre 2') NOT NULL,
    FOREIGN KEY (matricule) REFERENCES Etudiant(matricule) ON DELETE CASCADE,
    FOREIGN KEY (id_promo) REFERENCES Promotion(id_promo) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE Evaluer (
    id_evaluation INT AUTO_INCREMENT PRIMARY KEY,
    matricule CHAR(50),
    id_cours INT,
    TC FLOAT CHECK (TC BETWEEN 0 AND 10),
    Exam FLOAT CHECK (Exam BETWEEN 0 AND 10),
    FOREIGN KEY (matricule) REFERENCES Etudiant(matricule) ON DELETE CASCADE,
    FOREIGN KEY (id_cours) REFERENCES Cours(id_cours) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE Gerer (
    id_gestion INT AUTO_INCREMENT PRIMARY KEY,
    id_sec INT,
    id_promo INT,
    Semestre ENUM('Semestre 1', 'Semestre 2') NOT NULL,
    FOREIGN KEY (id_sec) REFERENCES SecJury(id_sec) ON DELETE CASCADE,
    FOREIGN KEY (id_promo) REFERENCES Promotion(id_promo) ON DELETE CASCADE
) ENGINE=InnoDB;
