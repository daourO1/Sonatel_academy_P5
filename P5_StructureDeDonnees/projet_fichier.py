from sys import exit
from proj_fonc import *
import json
import xml.etree.ElementTree as ET
import csv
import json
donnees_valides=[]
donnees_invalides=[]
booleen=True
#fichier=input("Vous voulez transformer votre fichier CSV en fichier XML ou en fichier JSON: ")
while booleen:
    fichier=input("Vous voulez transformer votre fichier CSV en fichier XML ou en fichier JSON: ")
    if fichier=='JSON':
        # nom du fichier CSV à lire
        chemin_fich_csv = "Donnees_Projet_Python_DataC5.csv"
        
        # nom du fichier JSON à écrire
        chemin_fich_json = "Donnees_Projet_Python_DataC5.json"
        
        # ouvrir le fichier CSV en mode lecture
        with open(chemin_fich_csv, 'r') as csv_file:
            # créer un lecteur CSV
            csv_reader = csv.DictReader(csv_file)
            # initialiser une liste pour stocker les données
            donneesJ = []
            # parcourir les lignes du fichier CSV
            for row in csv_reader:
                # ajouter la ligne à la liste des données
                donneesJ.append(row)
            #print(o"Les données CSV:\n",donnees)
        
        # ouvrir le fichier JSON en mode écriture
        with open(chemin_fich_json, 'w') as json_file:
            # écrire les données au format JSON dans le fichier
            dataJ=json.dumps(donnees)
            json_file.write(dataJ)
            data=json.loads(dataJ)
            #print()
            print("Les données JSON:\n",data)
            # for i in data:
            #     print(i)
        for etudiant in dataJ:
            #etudiant=[code,numero,nom,prenom,date_naissance,classe,note]
            cpt=0
            # Vérification de la validité de numéro etudiant
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
        # print("Les donnees invalide sont: \n",donnees_invalides)
        # print(len(donnees_invalides))
        # print()
        # print("Les donnees valide sont: \n",donnees_valides)
        # print(len(donnees_valides))
        ## Filtrer les données 
        choice=True
        while choice:
            print()
            print(100*'-')
            print(30*' ',"⏩ ⏩ ⏩ ⏩ ⏩   MENU   ⏪ ⏪ ⏪ ⏪ ⏪ ")
            print(100*'-')
            menu=affichage_menu()
            print(affichage_menu)
            print(100*'-')
            print()
            
            choix=input("Données votre choix: ")
            if choix=='1':
                print("Afficher les informations Valide de JSON en XML")
                chemin_fich_xml = "Donnees_validesJ_Python_DataC5.xml"
                liste_xml(donnees_validesJ,chemin_fich_xml)
                print()
            elif choix=='2':
                print("Afficher les informations Valide JSON en CSV")
                chemin_fich_csv = "Donnees_validesJ_Python_DataC5.csv"
                liste_csv(donnees_validesJ, chemin_fich_csv)
                print()
            elif choix=='3':
                print("Afficher les informations Invalide JSON en XML")
                chemin_fich_xml = "Donnees_invalidesJ_Python_DataC5.xml"
                liste_xml(donnees_invalidesJ,chemin_fich_xml)
                print()
            elif choix=='4':
                print("Afficher les informations Invalide de JSON en CSV")
                chemin_fich_csv = "Donnees_invalidesJ_Python_DataC5.csv"
                liste_csv(donnees_invalidesJ, chemin_fich_csv)
            exit
                
    if fichier=='XML':
        # nom du fichier CSV à lire
        chemin_fich_csv = "Donnees_Projet_Python_DataC5.csv"
        # ouvrir le fichier CSV en mode lecture
        with open(chemin_fich_csv, 'r') as csv_file:
            # créer un lecteur CSV
            csv_reader = csv.DictReader(csv_file)
            # initialiser une liste pour stocker les données
            
            donnees = []
            
            # parcourir les lignes du fichier CSV
            for row in csv_reader:
                # ajouter la ligne à la liste des données
                donnees.append(row)
            #print("Les données CSV:\n",donneesX)
            
                # nom du fichier XML à écrire
            chemin_fich_xml = "Donnees_Projet_Python_DataC5.xml"
            with open(chemin_fich_xml, 'w') as xml_file:
                xml_file.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no'?>)\n<Etudiants>")
                
                donneeX=""
                for etudiant in donnees:
                    
                    dataX='''
                    <etudiant>
                            <CODE> %s </CODE>
                            <Numero> %s </Numero>
                            <Nom> %s </Nom>
                            <Prenom> %s </Prenom>
                            <Date_de_naissance> %s </Date_de_naissance>
                            <Classe> %s </Classe>
                            <Note> %s </Note> 
                    </etudiant>''' %(etudiant["CODE"],etudiant["Numero"],etudiant["Nom"],etudiant["Prénom"],etudiant["Date de naissance"],etudiant["Classe"],etudiant["Note"])
                    donneeX+=dataX
                    
                    # écrire les données XML dans un fichier
                xml_file.write(donneeX)
                xml_file.write("<\n</Etudiants>")
                print("Les données XML: \n",donneeX)

            # ouvrir le fichier XML en mode lecture
            with open(chemin_fich_xml, 'r') as xml_file:
                # créer un arbre XML
                tree = ET.parse(xml_file)
                # obtenir la racine de l'arbre
                root = tree.getroot()
            
                # initialiser une liste pour stocker les données
                donneesX = []
            
                # parcourir les éléments de la racine
                for element in root:
                    # initialiser un dictionnaire pour stocker les données de l'élément
                    dict = {}
                    # parcourir les attributs de l'élément
                    for attribut in element.attrib:
                        # ajouter l'attribut au dictionnaire
                        dict[attribut] = element.attrib[attribut]
                    # parcourir les éléments enfants de l'élément
                    for sous_element in element:
                        # ajouter le sous-élément au dictionnaire
                        dict[sous_element.tag] = sous_element.text
                    # ajouter le dictionnaire à la liste des données
                    donneesX.append(dict)
            
            # afficher les données sous forme de liste de dictionnaires
            print("Les données XLM en dictionnaire : \n",donneesX)

            for etudiant in donneesX:
                #etudiant=[code,numero,nom,prenom,date_naissance,classe,note]
                cpt=0
                # Vérification de la validité de numéro etudiant
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
                    donnees_validesX.append(etudiant)
                else:
                    donnees_invalidesX.append(etudiant)
            # print("Les donnees invalide sont: \n",donnees_invalides)
            # print(len(donnees_invalides))
            # print("Les donnees valide sont: \n",donnees_valides)
            # print(len(donnees_valides))
            ## Filtrer les données
            choice=True
            while choice:
                print()
                print(100*'-')
                print(30*' ',"⏩ ⏩ ⏩ ⏩ ⏩   MENU   ⏪ ⏪ ⏪ ⏪ ⏪ ")
                print(100*'-')
                menu=affichage_menu1()
                print(affichage_menu1)
                print(100*'-')
                print()
                
                choix=input("Doneer votre choix: ")
                if choix=='1':
                    print("Afficher les informations Valide XML en JSON")
                    chemin_fich_json = "Donnees_validesX_Python_DataC5.xml"
                    liste_json(donnees_validesX,chemin_fich_json)
                    print()
                elif choix=='2':
                    print("Afficher les informations Valide XML en CSV")
                    chemin_fich_csv = "Donnees_validesX_Python_DataC5.csv"
                    liste_csv(donnees_validesX, chemin_fich_csv)
                    print()
                elif choix=='3':
                    print("Afficher les informations Invalide XML en JSON")
                    chemin_fich_json = "Donnees_invalidesX_Python_DataC5.xml"
                    liste_json(donnees_valides,chemin_fich_json)
                    print()
                elif choix=='4':
                    print("Afficher les informations Invalide XML en CSV")
                    chemin_fich_csv = "Donnees_invalidesX_Python_DataC5.csv"
                    liste_csv(donnees_invalides, chemin_fich_csv)
                    
                
                





