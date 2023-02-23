from sys import exit
from Exo8_Fonction import *
tab_mod=[]
e=0
choice=True
booleen=True
etudiant=[]
while booleen:
    nom=input("Donner votre nom: ")
    prenom=input("Donner votre prènom: ")
    classe=input("Donnez la classe: ")
    tel=input("Donner votre numero de telephone: ")
    veri=telephone(tel)
    while veri==False:
        print("Donner un bon numéro.")
        tel=input("Donner votre numero de telephone: ")
        veri=telephone(tel)
    dev=int(input("Donner votre note de devoir: "))
    veri=note_devoir(dev)
    while veri==False:
        print("Donner une bonne note.")
        dev=int(input("Donner votre note de devoir: "))
        veri=note_devoir(dev)
    proj=int(input("Donner votre note de projet: "))
    veri=note_projet(proj)
    while veri==False:
        print("Donner une bonne note.")
        proj=int(input("Donner votre note de projet: "))
        veri=note_projet(proj)
    exam=int(input("Donner votre note d'examen: "))
    veri=note_examen(exam)
    while veri==False:
        print("Donner une bonne note.")
        exam=int(input("Donner votre note d'examen: "))
        veri=note_examen(exam)
    moy=moyenne(dev,proj,exam,)


#creation tableau pour stocker les information de l'etudiant
    donnee=[prenom,nom,classe,tel,dev,proj,exam,moy]
    etudiant.append(donnee)
    reponse=input("Voulez vous entrer d'autres informations: ")
    if reponse=='oui':
        booleen=True
    else:
        booleen=False
#print(etudiant)
while choice:
    print()
    print(100*'-')
    print(50*' ',"MENU")
    print(100*'-')
    menu=affichage_menu()
    print(affichage_menu)

    choix=int(input("Vous voulez entrez dans quel menu: "))
    if choix==1:
        print('1-Afficher tout')
        print(tableau(etudiant))
    elif choix==2:
        print("2-Trier et afficher (par ordre décroissant de la moyenne")
        tableau(trie_etudiant(etudiant))
        
    elif choix==3:
        print("3-Rechercher selon un critère (téléphone, nom, prénom ou classe")
        critere=input("Vous voulez rechercher selon quelle critere: ")
        valeur=input("Element rechercher: ")
        rech=recherche(critere,valeur,etudiant)
        print(rech)
        #print(tableau(var))  
    elif choix==4:    
        print("4-Modification de notes pour un étudiant choisit par l’utilisateur en donnant le numéro de téléphone")
        val=input("Donner le numéro que vous voulez rechercher: ")
        new_note1 = int(input("Entrez la nouvelle note de devoir: "))
        new_note2 = int(input("Entrez la nouvelle note de projet: "))
        mod=modification(val,etudiant,new_note1,new_note2,tab_mod)
        print(mod)
    elif choix==5:
        print("5-Sortir (permet de terminer l’application")
        exit()
    else:
        print("Vous n'avez pas fait le bon choix.")


