#fonction téléphone
def telephone(tel):
    if len(tel)==9 and tel[:2] in ['77','78','76','75','70','33']:
        return True
    else:
        return False
# tel='77445443045'
# print(telephone(tel))

#fonction note devoirs
def note_devoir(dev):
    if 0<=dev<=20 and type(dev)==int:
        return True
    else:
        return False

#fonction note projet
def note_projet(proj):
    if 0<=proj<=20 and type(proj)==int:
        return True
    else:
        return False

#fonction note examen
def note_examen(exam):
    if 0<=exam<=20 and type(exam)==int:
        return True
    else:
        return False

#fonction moyenne
def moyenne(exam,dev,proj):
    return (exam+dev+proj)/3

#Fonction menu
def affichage_menu():
    print("1-Afficher tout")
    print("2-Trier et afficher (par ordre décroissant de la moyenne")
    print("3-Rechercher selon un critère (téléphone, nom, prénom ou classe")
    print("4-Modification de notes pour un étudiant choisit par l’utilisateur en donnant le numéro de téléphone")
    print("5-Sortir (permet de terminer l’application")


#fonction tableau
def tableau(etudiant):
    print(100*'-')
    print("|{0:<12} |{1:<12}|{2:<12}|{3:<12}|{4:<12}|{5:<12}|{6:<12}|{7:<12}".format("Prénom","Nom","Classe","Téléphone","Devoir","Projet","Examen","Moyenne"))
    print(100*'-')
    # print("Prénom", end="\t\t|")
    # print("Nom", end="\t|")
    # print("Classe",end="\t|")
    # print("Téléphone", end="\t|")
    # print("Devoir", end="\t|")
    # print("Projet", end="\t|")
    # print("Examen", end="\t|")
    # print("Moyenne")
    print(100*'-')
    for data in etudiant:
        prenom, nom, classe, tel, dev, proj, exam, moy = data
        print("|{0:<12} |{1:<12}|{2:<12}|{3:<12}|{4:<12.2f}|{5:<12.2f}|{6:<12.2f}|{7:<12.2f}".format(
            prenom, nom, classe, tel, dev, proj, exam, moy
        ))
        # print(prenom, end="\t|")
        # print(nom, end="\t|")
        # print(classe,end="\t|")
        # print(tel, end="     \t|")
        # print(dev, end="     \t|")
        # print(proj, end="     \t|")
        # print(exam, end="     \t|")
        # print("{:.2f}".format(moy))
    print(100*'-')
    print()
    print()

#fonction trie
def trie_etudiant(etudiant):
    for i in range(len(etudiant) - 1):
        for j in range(i + 1, len(etudiant)):
            if etudiant[i][7]< etudiant[j][7]:
                etudiant[i], etudiant[j] = etudiant[j], etudiant[i]           
    return etudiant
    # # Afficher les noms et les moyennes des étudiants
    # print(112*'-')
    # print("Prénom", end="\t|")
    # print("Nom", end="\t|")
    # print("Téléphone", end="\t|")
    # print("Devoir", end="\t|")
    # print("Projet", end="\t|")
    # print("Examen", end="\t|")
    # print("Moyenne")
    # print(112*'-')
    # for data in etudiant:
    #     prenom, nom, tel, dev, proj, exam, moy = data
    #     print(prenom, end="\t|")
    #     print(nom, end="\t|")
    #     print(tel, end="\t|")
    #     print(dev, end="\t|")
    #     print(proj, end="\t|")
    #     print(exam, end="\t|")
    #     print("{:.2f}".format(moy))
    #     print(112*'-')
    #return etudiant

#fonction recherche
def recherche(critere,valeur,etudiant):
    var=[]
    if critere=='telephone':
        
        veri=telephone(valeur)
        while veri==False:
            print("Donner un bon numéro.")
            valeur=input("Donner votre numero de telephone: ")
            veri=telephone(valeur)
        for data in etudiant:
            if data[3]==valeur:
                var.append(data)
       
    elif critere=='nom':
        for data in etudiant:
            if data[1]==valeur:
                var.append(data)
        
    elif critere=='prenom':
        for data in etudiant:
            if data[0]==valeur:
                var.append(data)
        
    elif critere=='classe':
        for data in etudiant:
            if data[2]==valeur:
                var.append(data)
    return(tableau(var))  

#Fonction modification
def modification(val,etudiant,new_note1,new_note2,tab_mod,exam):
    tab_mod=[]
    veri=telephone(val)
    while veri==False:
        print("Donner un bon numéro.")
        val=input("Donner votre numero de telephone: ")
        veri=telephone(val)
    for data in etudiant:
        if data[3] == val:
        # Demander à l'utilisateur de saisir les nouvelles notes
            # Modifier les notes pour l'étudiant correspondant
            data[4] = new_note1
            data[5] = new_note2
            data[7] =(new_note1+new_note2+exam)/3
            # Afficher la liste des entrées mise à jour
    for data in etudiant:
        tab_mod.append(data)
    return(tableau(tab_mod))


