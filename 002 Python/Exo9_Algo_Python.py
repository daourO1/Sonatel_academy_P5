from sys import exit
from Exo9_Fonction import *
matrice=[]
client=[]
booleen=True
choice=True
n = int(input("Combien d'opérateurs voulez-vous saisir?\n"))

# Saisir une suite d’ opérateurs téléphoniques
operateur_valide = ["orange", "tigo", "expresso","promobile"]
tab_op = []
for i in range(n):
    op = input("Donner les opérateurs téléphoniques" + str(i + 1) + ": ")
    while op.lower() not in operateur_valide:
        print("Veuillez saisir parmi les opérateurs suivants: orange, tigo, expresso.")
        op = input("Donner les opérateurs téléphoniques " + str(i + 1) + ": ")
    tab_op.append([op])
#print(tab_op)

for i in range(n):
    matrice.append([tab_op[i][0]])



# Saisi des informations du client
while booleen:
    nom=input("Donner votre nom: ")
    prenom=input("Donner votre prènom: ")
    tel=input("Donner votre numero de telephone: ")
    veri=telephone(tel)
    while veri==False:
        print("Donner un bon numéro.")
        tel=input("Donner votre numero de telephone: ")
        veri=telephone(tel)

    #creation tableau pour stocker les information d'un client
    donnee=[prenom,nom,tel]
    client.append(donnee)
    reponse=input("Voulez vous entrer d'autres informations: ")
    if reponse=='oui':
        booleen=True
    else:
        booleen=False


            
# Ranger les informations d’un client dans la ligne de l'opérateur correspondant à son numéro de téléphone.         
# for j in range(n):
#     for donnee in client:
#         if donnee[2][:2]=='77' or donnee[2][:2]=='78' and tab_op[j][0] == "orange":
#             tab_op[j].append(donnee)
#                 # matrice[j].append(client[i])
#             #break
#         elif donnee[2][:2]=='76' and tab_op[j][0] == "tigo":
#             tab_op[j].append(donnee)
#             #break
#         if donnee[2][:2]=='70' and tab_op[j][0] == "expresso":
#             tab_op[j].append(donnee)
#             #break
#         if donnee[2][:2]=='75' and tab_op[j][0] == "promobile":
#             tab_op[j].append(donnee)
#             #break
        

# # Affichage de la matrice
# for i in range(n):
#     print("\t", tab_op[i])

# Les affichages
while choice:
    print()
    print(100*'-')
    print(50*' ',"MENU")
    print(100*'-')
    menu=affichage_menu()
    print(affichage_menu)
    choix=int(input("Vous voulez entrez dans quel menu: "))
    if choix==1:
        print('1-Afficher les clients de la matrice par opérateurs')
        for i in range(len(client)):
            tel = client[i][2]
            op = operateur(tel)
            indice = tab_op.index([op])
            matrice[indice].append(client[i])

            # Affichage du résultat final
        for i in range(n):
            print("Opérateur téléphonique:", tab_op[i][0])
            print("Nombre de clients:", len(matrice[i]) - 1)
            for j in range(1, len(matrice[i])):
                print("Nom:", matrice[i][j][1], "Prénom:", matrice[i][j][0], "Numéro de téléphone:", matrice[i][j][2])
        print("\n")
    elif choix==2:
        print("2-Afficher les clients d’un opérateur")
        choice = True
        while choice:
            op = input("Entrer le nom de l'opérateur pour lequel vous voulez voir les clients: ")
            indice = tab_op.index([op])
            print("Opérateur téléphonique:", tab_op[indice][0])
            print("Nombre de clients:", len(matrice[indice]) - 1)
            for i in range(1, len(matrice[indice])):
                print("Nom:", matrice[indice][i][1], "Prénom:", matrice[indice][i][0], "Numéro de téléphone:", matrice[indice][i][2])
            print("\n")
            ask = input("Voulez-vous voir pour un autre opérateur? (oui/non) ")
            if ask == "non":
                choice = False
            exit(0)
    elif choix==3:
        print("3-Afficher les numéros téléphone d’un client")
        while choice:
            nom = input("Entrer le nom du client: ")
            prenom = input("Entrer le prénom du client: ")
            trouve = False
            for i in range(len(client)):
                if client[i][1] == nom and client[i][0] == prenom:
                    print("Numéro de téléphone du client:", client[i][2])
                trouve = True
            if not trouve:
                print("Le client n'a pas été trouvé.")
            reponse = input("Voulez-vous afficher les numéros téléphone d'un autre client: ")
            if reponse == 'oui':
                choice = True
            else:
                choice = False
            exit(0)
    elif choix==4:
        print("4-Modifier ou ajouter un numero telephone pour un client")
        nom = input("Donner le nom du client pour lequel vous voulez modifier le numéro de téléphone: ")
        prenom = input("Donner le prénom du client pour lequel vous voulez modifier le numéro de téléphone: ")
        nouveau_tel = input("Donner le nouveau numéro de téléphone: ")
        verif = telephone(nouveau_tel)
        while verif == False:
            print("Donner un bon numéro.")
            nouveau_tel = input("Donner le nouveau numéro de téléphone: ")
            verif = telephone(nouveau_tel)

        resultat = modifier_numero(client, nom, prenom, nouveau_tel)
        if resultat == False:
            print("Client non trouvé.")
        else:
            print("Numéro de téléphone modifié avec succès.")
    elif choix==5:
        print("5-Sortir (permet de terminer l’application")
        exit()
    else:
        print("Vous n'avez pas fait le bon choix.")

