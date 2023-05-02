sudo mysql

--  EXPORTER ET RESTAURER UN BD
-- Faites un import de la BD “odc_recette_cours.sql”
CREATE DATABASE odc_recette_cours;

use odc_recette_cours;

source /home/daour/Sonatel_academy_P5/007 Conception et administration d_une base de données SQL/Projet_SQL/odc_recette_cours.sql;

SHOW TABLES;

DESCRIBE amende;
DESCRIBE contribuable;
DESCRIBE declaration;
DESCRIBE migration_versions;
DESCRIBE payer_amende;
DESCRIBE payer_taxe;
DESCRIBE quittance;
DESCRIBE taxes;

--  LANGAGE D'INTERROGATION DE DONNEES (LID) : SELECT ;
-- o Projection
-- o Restriction
-- o Jointure
-- o Alias (AS)
-- Donner le nom et l’adresse des contribuables qui ont fait des déclarations
-- publicitaires
-- SELECT DISTINCT contribuable.nom, contribuable.adr 
--  on pouver aussi utiliser le DISTINCT pour supprimer les doublons
SELECT contribuable.nom, contribuable.adr
FROM contribuable
INNER JOIN declaration ON contribuable.ncont = declaration.ncont
WHERE declaration.libelle = 'publicité';


-- o Sous requête
-- Donner le numéro et le nom du premier contribuable qui a payé une amende
-- SELECT contribuable.ncont, contribuable.nom
-- FROM contribuable
-- INNER join payer_amende ON contribuable.ncont = payer_amende.ncont
-- LIMIT 1;
SELECT ncont, nom
FROM contribuable
WHERE ncont = (SELECT ncont FROM payer_amende ORDER BY date ASC LIMIT 1);


-- o Fonctions d'agrégation
-- - SUM
-- Donner le numéro, le nom, le libellé et le montant totale de l’amande payé pour
-- chaque contribuable selon le type(libellé) d’amande
SELECT contribuable.ncont, contribuable.nom, amende.libelle, SUM(amende.montant)
FROM contribuable
INNER JOIN payer_amende ON contribuable.ncont = payer_amende.ncont
INNER JOIN amende ON payer_amende.namende = amende.namende
GROUP BY contribuable.ncont, contribuable.nom, amende.libelle


-- -AVG
-- Donner le numéro, le nom et le montant moyen des taxes payées par chaque
-- contribuable
SELECT contribuable.ncont, nom, AVG(taxes.montant)
FROM contribuable
INNER JOIN payer_taxe ON contribuable.ncont = payer_taxe.ncont
INNER JOIN taxes ON payer_taxe.ntaxe = taxes.ntaxe
GROUP BY contribuable.ncont, contribuable.nom;


-- -MIN
-- Donner le numéro, le nom le libellé et le montant des contribuables ayant payé
-- l’amande minimale
SELECT contribuable.ncont, contribuable.nom, amende.libelle, MIN(amende.montant)
FROM contribuable
INNER JOIN payer_amende ON contribuable.ncont = payer_amende.ncont
INNER JOIN amende ON payer_amende.namende = amende.namende
GROUP BY contribuable.ncont, contribuable.nom, amende.libelle;


-- -MAX
-- Donner le numéro, le nom le libellé et le montant des contribuables ayant payé la
-- taxe maximale
SELECT contribuable.ncont, nom, declaration.libelle, MAX(taxes.montant)
FROM contribuable
INNER JOIN payer_taxe ON contribuable.ncont = payer_taxe.ncont
INNER JOIN declaration ON contribuable.ncont = declaration.ncont
INNER JOIN taxes ON payer_taxe.ntaxe = taxes.ntaxe
GROUP BY contribuable.ncont, contribuable.nom, declaration.libelle;


-- o Commande
-- - ORDER BY
-- Donner le numéro, le nom le libellé et le montant des 5(cinq) premiers
-- contribuables ayant payé la taxe maximale
SELECT contribuable.ncont, nom, declaration.libelle, MAX(taxes.montant)
FROM contribuable
INNER JOIN payer_taxe ON contribuable.ncont = payer_taxe.ncont
INNER JOIN declaration ON contribuable.ncont = declaration.ncont
INNER JOIN taxes ON payer_taxe.ntaxe = taxes.ntaxe
GROUP BY contribuable.ncont, contribuable.nom, declaration.libelle, payer_taxe.date
ORDER BY payer_taxe.date ASC
LIMIT 5;


-- -GROUP BY
-- Donner le libelle de la déclaration, le montant de la taxe et le nom du
-- contribuable des taxes payées le 2020-06-05
SELECT declaration.libelle, taxes.montant, contribuable.nom
FROM declaration
INNER JOIN contribuable ON declaration.ncont = contribuable.ncont
INNER JOIN payer_taxe ON contribuable.ncont = payer_taxe.ncont
INNER JOIN taxes ON payer_taxe.ntaxe = taxes.ntaxe
WHERE payer_taxe.date = '2020-06-05'
GROUP BY declaration.libelle, taxes.montant, contribuable.nom;


-- -HAVING
-- Donner le numéro et le nom des contribuables qui ont individuellement payé au
-- total plus de 500.000F d’amende pour des déclarations de spectacles.
SELECT contribuable.ncont, contribuable.nom, SUM(amende.montant) AS total_amendes
FROM contribuable 
INNER JOIN payer_amende ON contribuable.ncont = payer_amende.ncont
INNER JOIN amende ON payer_amende.namende = amende.namende
INNER JOIN declaration ON contribuable.ncont = declaration.ncont
WHERE declaration.libelle = 'Spectacle'
GROUP BY contribuable.ncont, contribuable.nom
HAVING total_amendes > 500000;
-- HAVING serre à filtrer