from sys import exit
from poo_fonction import *
import json
import xml.etree.ElementTree as ET
import csv
import json

donnees_validesJ=[]
donnees_invalidesJ=[]
donnees_validesX=[]
donnees_invalidesX=[]
booleen=True
#fichier=input("Vous voulez transformer votre fichier CSV en fichier XML ou en fichier JSON: ")
while booleen:
    fichier=input("Vous voulez transformer votre fichier CSV en fichier XML ou en fichier JSON: ")
    if fichier=='JSON':
        booleen=False
        tabJ=[]
        t=transformation_csv()
        tabJ=t.csv_json()
        print(tabJ)
        for etudiant in tabJ:
            #etudiant=[code,numero,nom,prenom,date_naissance,classe,note]
            cpt=0
            # Vérification de la validité de numéro etudiant
            veri=verification("numero","nom","prenom","date_naissance","classe","note")
            veri.numero_etudiant()
            if numero_etudiant(etudiant["Numero"])==True:
                cpt+=1
            else:
                etudiant["Motif"]='Numéro invalide'
                #donnees_invalides.append(etudiant)
                # Vérification de la validité de nom etudiant
            if nom_etudiant(etudiant["Nom"])==True:
                cpt+=1
            else:
                etudiant["Motif"]="Nom invalide"
                #donnees_invalides.append(etudiant)
                # Vérification de la validité de prénom etudiant
            if prenom_etudiant(etudiant["Prénom"])==True:
                cpt+=1
            else:
                etudiant["Motif"]="Prénom invalide"
                #donnees_invalides.append(etudiant)
                # Vérification de la validité de la date de naissance de etudiant
            if date_naissance_etudiant(etudiant["Date de naissance"])==True:
                cpt+=1
            else: 
                etudiant["Motif"]="Date de naissance invalide"
                #donnees_invalides.append(etudiant)
                # Vérification de la validité de classe etudiant
            if classe_etudiant(etudiant["Classe"])==True:
                cpt+=1
            else:
                etudiant["Motif"]="Classe invalide"
                #donnees_invalides.append(etudiant)
                # Vérification de la validité de note etudiant
            if note_etudiant(etudiant["Note"])==True:
                cpt+=1
            else:
                etudiant["Motif"]="Note invalide"
                #donnees_invalides.append(etudiant)
                    # Si toutes les données sont valides, on ajoute les données à la liste des données valides
            if cpt==(len(etudiant)-1):
                donnees_validesJ.append(etudiant)
            else:
                donnees_invalidesJ.append(etudiant)
        # print("Les donnees invalide sont: \n",donnees_invalidesJ)
        # print(len(donnees_invalides))
        # print()
        # print("Les donnees valide sont: \n",donnees_validesJ)
        # print(len(donnees_valides))
        choice=True
        while choice:
            menu = affichage("option")
            menu.en_tete()
            menu.affichage_menu()
            print(100*'-')
            print()
            choix=int(input("Vous voulez entrez dans quel menu: "))
            if choix==1:
                print("Afficher les informations Valide")
    elif fichier=='XML':
        booleen=False
        tab=[]
        t=transformation_csv()
        tab=t.csv_xml()
        print(tab)
        menu = affichage("option")
        menu.en_tete()
        menu.affichage_menu()
        print(100*'-')
        print()
        
    else:
        print("Choisisez entre JSON et CSV")
                





