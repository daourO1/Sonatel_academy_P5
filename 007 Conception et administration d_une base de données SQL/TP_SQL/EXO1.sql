-- sudo mysql

--  Création de la base et ses tables
CREATE DATABASE Piece_Vehicule;

CREATE TABLE vehicule
(
id_vehicule    INT AUTO_INCREMENT PRIMARY KEY,
marque         VARCHAR(15),
modele         VARCHAR(15),
annee          INT(4)
);

CREATE TABLE reference
(
id_reference    INT PRIMARY KEY AUTO_INCREMENT,
prix         VARCHAR(15)
);

CREATE TABLE piece
(
id_piece    INT PRIMARY KEY AUTO_INCREMENT,
categorie         VARCHAR(15),
date_recup         DATE,
id_reference      INT,
FOREIGN KEY (id_reference) REFERENCES reference (id_reference)
);

CREATE TABLE convenance
(
id_vehicule    INT,
id_piece       INT,
FOREIGN KEY (id_vehicule) REFERENCES vehicule (id_vehicule),
FOREIGN KEY (id_piece) REFERENCES piece (id_piece)
);

-- Pour voir toutes lesbases
use DATABASES
-- Pour voir une base precis
use Piece_Vehicule;
-- Pour voir les tables
SHOW TABLES;
-- Pour voir une tables 
DESCRIBE vehicule;

-- Remplir les tables
INSERT INTO vehicule (id_vehicule, marque, modele, annee) VALUES ('1','Toyota', 'Corolla', '2022');
INSERT INTO vehicule (id_vehicule, marque, modele, annee) VALUES ('2','Honda', 'Civic', '2021');
INSERT INTO vehicule (id_vehicule, marque, modele, annee) VALUES ('3','Chevrolet', 'Camaro', '2019');
-- Pour voir les valeurs de la table
SELECT * FROM vehicule;
-- Pour supprimer les valeurs d'une table
DELETE FROM vehicule;

DESCRIBE reference;
INSERT INTO reference (id_reference, prix) VALUES ('1','10000');
INSERT INTO reference (id_reference, prix) VALUES ('2','15000');
INSERT INTO reference (id_reference, prix) VALUES ('3','20000');
SELECT * FROM reference;

DESCRIBE piece;
INSERT INTO piece (id_piece, categorie, date_recup, id_reference) VALUES ('1','carosserie','2022/02/12','1');
INSERT INTO piece (id_piece, categorie, date_recup, id_reference) VALUES ('2','mécanique','2021/03/01','2');
INSERT INTO piece (id_piece, categorie, date_recup, id_reference) VALUES ('3','électricité','2019/12/09','3');
SELECT * FROM piece;

DESCRIBE convenance;
INSERT INTO convenance (id_vehicule, id_piece) VALUES ('1','1');
INSERT INTO convenance (id_vehicule, id_piece) VALUES ('2','2');
INSERT INTO convenance (id_vehicule, id_piece) VALUES ('3','3');
SELECT * FROM convenance;

