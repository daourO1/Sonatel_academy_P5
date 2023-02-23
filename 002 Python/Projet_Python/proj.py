from sys import exit
from proj_fonc import *
# Importer le module csv :
import csv
donnees_valides=[]
donnees_invalides=[]
# ouvrir le fichier CSV en utilisant la méthode open()
with open('Donnees_Projet_Python_DataC5.csv', 'r') as csvfile:
    # Transformer le fichier CSV en liste, vous pouvez utiliser le module csv et sa méthode reader()
    csvreader = csv.reader(csvfile)
    # Une variable qui contiendra maintenant toutes les données du fichier CSV sous forme de liste
    donnees=list(csvreader)
    #print(donnee)
    # Parcourir la liste et l'afficher
    # en_tete=donnee[0]
    # print(en_tete)
    donnee=donnees[1:]
    for etudiant in donnee:
        code=etudiant[0]
        numero=etudiant[1]
        nom=etudiant[2]
        prenom=etudiant[3]
        date_naissance=etudiant[4]
        classe=etudiant[5]
        note=etudiant[6]
        #etudiant=[code,numero,nom,prenom,date_naissance,classe,note]
        cpt=0
        # Vérification de la validité de numéro etudiant
        if numero_etudiant(etudiant[1])==True:
            cpt+=1
        else:
            etudiant.append("Numéro invalide")
            #donnees_invalides.append(etudiant)
            # Vérification de la validité de nom etudiant
        if nom_etudiant(etudiant[2])==True:
            cpt+=1
        else:
            etudiant.append("Nom invalide")
            #donnees_invalides.append(etudiant)
            # Vérification de la validité de prénom etudiant
        if prenom_etudiant(etudiant[3])==True:
            cpt+=1
        else:
            etudiant.append("Prénom invalide")
            #donnees_invalides.append(etudiant)
           # Vérification de la validité de la date de naissance de etudiant
        if date_naissance_etudiant(etudiant[4])==True:
            cpt+=1
        else:
            etudiant.append("Date de naissance invalide")
            #donnees_invalides.append(etudiant)
            # Vérification de la validité de classe etudiant
        if classe_etudiant(etudiant[5])==True:
            cpt+=1
        else:
            etudiant.append("Classe invalide")
            #donnees_invalides.append(etudiant)
            # Vérification de la validité de note etudiant
        if note_etudiant(etudiant[6])==True:
            cpt+=1
        else:
            etudiant.append("Note invalide")
            #donnees_invalides.append(etudiant)
                # Si toutes les données sont valides, on ajoute les données à la liste des données valides
        if cpt==(len(etudiant)-1):
            donnees_valides.append(etudiant)
        else:
            donnees_invalides.append(etudiant)
    # print("Les donnees invalide sont: \n",donnees_invalides)
    # print(len(donnees_invalides))
    # print("Les donnees valide sont: \n",donnees_valides)
    # print(len(donnees_valides))
    
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
    
    choix=int(input("Vous voulez entrez dans quel menu: "))
    if choix==1:
        print("1-D’afficher les informations Valide")
        veri=remplacer_notes_par_moyennes(donnees_valides)
        print(tableau(veri))
    elif choix==2:
        print("2-D’afficher les informations inValide")
        print(donnees_invalides)
    elif choix==3:
        print("3-D’afficher une information (par son numéro)")
        valeur=input("Entrer le numéro rechercher: ")
        rech=recherche(valeur,donnee)
        print(rech)
    elif choix==4:
        print("4-D’afficher les cinq premier")
        veri=remplacer_notes_par_moyennes(donnees_valides)
        tab=trie_etudiant(veri)
        print(tableau(tab[:5]))
    elif choix==5:
        print("5-D’ajouter une information en vérifiant la validité des informations données.")
        code=input("Donner son code")
        numero=input("Donner son numero")
        veri=numero_etudiant(numero)
        while veri==False:
            print("Donner un bon numéro.")
            numero=input("Donner son numero")
            veri=numero_etudiant(numero)
        
        nom=input("Donner son nom")
        veri=nom_etudiant(nom)
        while veri==False:
            print("Donner un bon nom.")
            nom=input("Donner son nom")
            veri=nom_etudiant(nom)
        
        prenom=input("Donner son prenom")
        veri=prenom_etudiant(prenom)
        while veri==False:
            print("Donner un bon prenom.")
            prenom=input("Donner son prenom")
            veri=prenom_etudiant(prenom)
            
        date_naissance=input("Donner son date_naissance")
        veri=date_naissance_etudiant(date_naissance)
        while veri==False:
            print("Donner une bonne date_naissance.")
            date_naissance=input("Donner son date_naissance")
            veri=date_naissance_etudiant(date_naissance)
            
        classe=input("Donner son classe")
        veri=classe_etudiant(classe)
        while veri==False:
            print("Donner une bonne classe.")
            classe=input("Donner son classe")
            veri=classe_etudiant(classe)
            
        note=input("Donner son note")
        veri=note_etudiant(note)
        while veri==False:
            print("Donner une bonne note.")
            note=input("Donner son note")
            veri=note_etudiant(note)
            
        new_etudiant=[code,numero,nom,prenom,date_naissance,classe,note]
        donnee.append(new_etudiant)
    elif choix==6:
        print("6-De modifier une information invalide ensuite le transférer dans la structure où se trouve les informations valides")
        
        code=input("Donner le code que vous voulez rechercher: ")
        for etudiant in donnees_invalides:
            while code not in etudiant:
                print("Ce code n'est pas dans la liste des donnees invalides.")
                code=input("Donner le code que vous voulez rechercher: ")
            if etudiant[0]==code:
                donnees_invalides.remove(etudiant)
            
        mod_numero=input("Donner son numero")
        veri=numero_etudiant(numero)
        while veri==False:
            print("Donner un bon numéro.")
            mod_numero=input("Donner son numero")
            veri=numero_etudiant(numero)
        
        mod_nom=input("Donner son nom")
        veri=nom_etudiant(nom)
        while veri==False:
            print("Donner un bon nom.")
            mod_nom=input("Donner son nom")
            veri=nom_etudiant(nom)
        
        mod_prenom=input("Donner son prenom")
        veri=prenom_etudiant(prenom)
        while veri==False:
            print("Donner un bon prenom.")
            mod_prenom=input("Donner son prenom")
            veri=prenom_etudiant(prenom)
            
        mod_date_naissance=input("Donner son date_naissance")
        veri=date_naissance_etudiant(date_naissance)
        while veri==False:
            print("Donner une bonne date_naissance.")
            mod_date_naissance=input("Donner son date_naissance")
            veri=date_naissance_etudiant(date_naissance)
            
        mod_classe=input("Donner son classe")
        veri=classe_etudiant(classe)
        while veri==False:
            print("Donner une bonne classe.")
            mod_classe=input("Donner son classe")
            veri=classe_etudiant(classe)
            
        mod_note=input("Donner son note")
        veri=note_etudiant(note)
        while veri==False:
            print("Donner une bonne note.")
            mod_note=input("Donner son note")
            veri=note_etudiant(note)
            
        mod_etudiant=[code,mod_numero,mod_nom,mod_prenom,mod_date_naissance,mod_classe,mod_note]
        donnees_valides.append(mod_etudiant) 
    else:
        print("Vous n'avez pas fait le bon choix.")

        

    #exit()
        
        

