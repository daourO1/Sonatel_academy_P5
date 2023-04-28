CREATE DATABASE Piece_Vehicule;
use Piece_Vehicule;

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

-- Pour voir les tables
SHOW TABLES;

-- Pour voir une tables 
DESCRiBE convenance;



