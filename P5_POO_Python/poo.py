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
        #print(tabJ)
        for etudiant in tabJ:
            code=etudiant["CODE"]
            numero=etudiant["Numero"]
            nom=etudiant["Nom"]
            prenom=etudiant["Prénom"]
            date_naissance=etudiant["Date de naissance"]
            classe=etudiant["Classe"]
            note=etudiant["Note"]
            cpt=0
            # Vérification de la validité de numéro etudiant
            veri=verification(numero,nom,prenom,date_naissance,classe,note)
            if veri.numero_etudiant(numero)==True:
                cpt+=1
            else:
                etudiant["Motif"]='Numéro invalide'
                #donnees_invalides.append(etudiant)
                # Vérification de la validité de nom etudiant
            if veri.nom_etudiant(nom)==True:
                cpt+=1
            else:
                etudiant["Motif"]="Nom invalide"
                #donnees_invalides.append(etudiant)
                # Vérification de la validité de prénom etudiant
            if veri.prenom_etudiant(prenom)==True:
                cpt+=1
            else:
                etudiant["Motif"]="Prénom invalide"
                #donnees_invalides.append(etudiant)
                # Vérification de la validité de la date de naissance de etudiant
            if veri.date_naissance_etudiant(date_naissance)==True:
                cpt+=1
            else: 
                etudiant["Motif"]="Date de naissance invalide"
                #donnees_invalides.append(etudiant)
                # Vérification de la validité de classe etudiant
            if veri.classe_etudiant(classe)==True:
                cpt+=1
            else:
                etudiant["Motif"]="Classe invalide"
                #donnees_invalides.append(etudiant)
                # Vérification de la validité de note etudiant
            if veri.note_etudiant(note)==True:
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
        # # print()
        # print("Les donnees valide sont: \n",donnees_validesJ)
        # print(len(donnees_valides))
        for etudiant in donnees_validesJ:
            note=etudiant["Note"]
            d=note_moyenne(note,donnees_validesJ)
            d.moyenne(note)
            d.remplacer_notes_par_moyennes(donnees_validesJ)
            etudiant.pop("Note")
        dv=d.remplacer_notes_par_moyennes(donnees_validesJ)
        # print(dv)
        choice=True
        while choice:
            menu = affichage("optionJ","optionX")
            menu.en_tete()
            menu.affichage_menuJ()
            print(100*'-')
            print()
            choix=int(input("Vous voulez entrez dans quel menu: "))
            if choix==1:
                print("Transformation données valides JSON en XML")
                chemin_fich_xml = "Donnees_validesJ.xml"
                mod=transformation()
                mod.liste_xml(dv,chemin_fich_xml)
            elif choix==2:
                print("Transformation données valides JSON en CSV")
                chemin_fich_csv = "Donnees_validesJ.csv"
                mod=transformation()
                mod.liste_csv(dv,chemin_fich_csv)

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
                





