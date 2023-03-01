from datetime import datetime
import re
import json
import xml.etree.ElementTree as ET
import csv

def affichage_menu():
    print("   1-  D’afficher les informations Valide ")
    print("   2-  D’afficher les informations invalide ")
    print("   3-  D’afficher une information (par son numéro)")
    print("   4-  D’afficher les cinq premierModificatios")
    print("   5-  D’ajouter une information en vérifiant la validité des informations données.")
    print("   6-  De modifier une information invalide ensuite le transférer dans la structure où se trouve les informations valides")

## Fontion pour les numéros
#numero='12QSDF3'
def numero_etudiant(numero):
    if not numero:
        return False
    import re
    # Vérifier si le numéro est valide en utilisant l'expression régulière
    regex = r'^[A-Z0-9]{7}$'
    if re.match(regex, numero):
        return True
    else:
        return False


## Fonction prénom
#prenom='ghjao'
def prenom_etudiant(prenom):
    if not prenom:
        return False
    import re
    regex_prenom = r'^[A-Za-z][A-Za-z ]{2,}$'
    if re.match(regex_prenom, prenom):
        return True
    else:
        return False


## Fonction nom
#nom='Cyrille  '
def nom_etudiant(nom):
    if not nom:
        return False
    
    import re
    regex_nom = r'^[A-Z][A-Za-z ]{1,}$'
    if re.match(regex_nom, nom):
        return True
    else:
        return False
# veri=nom_etudiant(nom)
# print(veri)
  

## Fonction date de naissance
#date_naissance='16/08/99'
def date_naissance_etudiant(date_naissance):
    if not date_naissance:
        return False
    c=['/','-','_',',','|',':','.',' ']
    date=''
    date1=''
    date_naissance1=""
    date_new=""
    new_date=""
    naissance=""
    new_naissance=""
    # Supprime les espace inutiles
    for i in range(len(date_naissance)):
        if date_naissance[i]==' ' and date_naissance[i+1]==' ':
            continue 
        else:
            date+=date_naissance[i]
    #print(date)
    # vérifie si le premier caractère n'est pas un chiffre
    if not date[0].isdigit():  
        # supprime le premier caractère de la chaîne
        date_new = date[1:]  
    else:
        date_new=date
    #print(date_new)
    # Créer une table de traduction qui remplace tous les caractères de la liste c par /
    table = str.maketrans(dict.fromkeys(c, '/'))
    # Appliquer la table de traduction à la chaîne de caractères new_date
    naissance = date_new.translate(table)
    #print(naissance)
    # Supprime les '/' inutiles
    for i in range(len(naissance)):
        if naissance[i]=='/' and naissance[i+1]=='/':
            continue
        else:
            new_naissance+=naissance[i]
    #print(new_naissance)
    # Verifier si la date respecte le format jour/mois/année
    format_string = "%d/%m/%y"
    try:
        new_naissance=datetime.strptime(new_naissance, format_string)
        return True
    except ValueError:
        return False
# veri=date_naissance_etudiant(date_naissance)
# print(veri)



#classe='  1 iem A'
def classe_etudiant(classe):
    if not classe:
        return False
    classe1=""
    for i in range(len(classe)):
        if classe[i]==' ':
            continue 
        else:
            classe1+=classe[i]
    if classe1[0] in ['3','4','5','6']:
        #print(classe1)
        p3=r'3'
        p4=r'4'
        p5=r'5'
        p6=r'6'
        classe_p3=re.match(p3, classe1)
        classe_p4=re.match(p4, classe1)
        classe_p5=re.match(p5, classe1)
        classe_p6=re.match(p6, classe1)
        if classe_p3:
            var=re.sub(r'[3]([a-z]+)','3eme',classe1)
        elif classe_p4:
            var=re.sub(r'[4]([a-z]+)','4eme',classe1)
        elif classe_p5:
            var=re.sub(r'[5]([a-z]+)','5eme',classe1)
        elif classe_p6:
            var=re.sub(r'[6]([a-z]+)','6eme',classe1)
        #print(var)
        if var[-1] in ['A','B']:
            return True
        else:
            return False
    else:
        return False
    return True
# veri=classe_etudiant(classe)
# print(veri)

## Fonction note etudiant
#note='PC[11|10|9:10]#Math[11|10|12:10]#Francais[10:9]#Anglais[12:111]#SVT[10|12|8:12]#HG[11:13]'
def note_etudiant(note):
    if not note:
        return False
    
    note4 = []
    note1 = note.strip()
    note2 = note1.replace("]", "").replace("|", " ").replace(",", ".")
    note3 = note2.split("#")
    for i in note3:
        if i=="":
            note3.remove(i)
    for i in note3:
        matière = i.split("[")
        if len(matière) != 2:
            return False
        note4.append([matière[0].strip(), matière[1].strip()])
    #print(note4)
    for matière in note4:
        #print(matière)
        if matière[0].isalpha():
            examens = matière[1].split(':')
            #print(examens)
            if len(examens) != 2:
                return False
            else:
                devoirs = examens[0].split()
                #print(devoirs)
                validite_notes = True
                for devoir in devoirs:
                    #print(devoir)
        #         if not devoir.isnumeric():
        #             return False
                    for i in devoir:
                        if not i.isnumeric() and i!='.':
                            return False
                    if not (0 <= float(devoir) <= 20):
                        validite_notes = False
                        if not (0 <= float(examens[1]) <= 20):
                            validite_notes = False
                        if not validite_notes:
                            return False

    return True
# veri=note_etudiant(note)
# print(veri)

#note='Math[10|11:15] #Francais[7|12|8:13] #Anglais[13,5|9:15] #PC[11:9]  #SVT[12|9|16|11:12]  #HG[10:13]'
# Fonction Calcul moyen
def moyenne(note):
    note1 = note.strip()
    note2 = note1.replace("]", "").replace("|", " ").replace(",", ".")
    note3 = note2.split("#")
    note4 = []
    note5 = []
    matières={}
    new_donnees_valides=[]
    for i in note3:
        matière = i.split("[")
        if len(matière)==2:
            note4.append([matière[0].strip(), matière[1].strip()])
    moy_G=0
    count=0
    for matière in note4:
        if matière[0].isalpha():
            examens = matière[1].split(':')
            devoirs = examens[0].split()
            not_dev = [float(x) for x in devoirs]
            #print(not_dev)
            moyenne = sum(not_dev) / len(not_dev)
            #print(moyenne)
            examen = examens[1]
            #print(examen)
            moy_G1 =((moyenne+(2*float(examen)))/3)
            moy_G1=round(moy_G1,3)
            #print(moy_G1)
            moy_G += moy_G1
            #print(moy_G)
            #count += 1
            #print(len(note4))    
    #print(moy_G)
    moyenne_G = moy_G / len(note4) 
    moyenne_G = round(moyenne_G, 3)
    # print(moyenne_G)
    return moyenne_G
    # for etudiant in donnees_valides:
    #     code,numero,nom,prenom,date_naissance,classe,note=etudiant
    #     etudiant.remove(note)
    #     etudiant.append(moy_G)
    # new_donnees_valides.append(etudiant)
        
            
    #         examens.append(moy_G)
    #         #print(moy_G)
    #         matières[matière[0]]=examens
    # note5.append(matières)
    
    #print(note5)
            
            #for devoir in devoirs:
                
            # if not (0 <= float(examens[1]) <= 20):
            #     validite_notes = False
            # if not validite_notes:
            #     return False
    #return moy_G
# veri=moyenne(note)
# print(veri)

def remplacer_notes_par_moyennes(donnees_valides):
    new_donnees_valides = []
    for etudiant in donnees_valides:
        code,numero,nom,prenom,date_naissance,classe,note=etudiant
        moyenne_generale = moyenne(note)
        new_donnees_valides.append((code,numero,nom,prenom,date_naissance,classe, moyenne_generale))
    return new_donnees_valides

 
def tableau(donnee):
    print(140*'-')
    print("|{0:<20}|{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}".format("Code","Numéro","Nom","Prénom","Date de naissance","Classe","Moyenne Etudiant"))
    print(140*'-')
    
    for etudiant in donnee:
        code,numero,nom,prenom,date_naissance,classe,note=etudiant
        print("|{0:<20}|{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}".format(
            code,numero,nom,prenom,date_naissance,classe,note
        ))
        
    print(140*'-')
    print()
    print()
    
def tableau1(donnee):
    print(100*'-')
    print("|{0:<20} |{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}|{7:<20}|{8:<20}".format("Code","Numéro","Nom","Prénom","Date de naissance","Classe","Note","Motif d'invalidité"))
    print(100*'-')
    
    print(100*'-')
    for etudiant in donnee:
        code,numero,nom,prenom,date_naissance,classe,note,motif=etudiant
        print("|{0:<20} |{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}|{7:<20}".format(
            code,numero,nom,prenom,date_naissance,classe,note,motif
        ))
        
    print(100*'-')
    print()
    print()


#fonction recherche
def recherche(valeur,donnee):
    var=[]
    #veri=numero_etudiant(valeur)
    for etudiant in donnee:
        
        # while etudiant[1]!=valeur:
        #     print("Ce numéro n'existe pas dans la base")
        #     valeur=input("Donner un autre numéro: ")
        # for etudiant in donnee:
        if etudiant[1]==valeur:
            var.append(etudiant)
        else:
            print("Ce numéro n'existe pas dans la base")
                
    return var

## Fonction trie
def trie_etudiant(donnees_valides):
    for i in range(len(donnees_valides) - 1):
        for j in range(i + 1, len(donnees_valides)):
            if donnees_valides[i][6]< donnees_valides[j][6]:
                donnees_valides[i], donnees_valides[j] = donnees_valides[j], donnees_valides[i]           
    return donnees_valides


## pagination
def affichage_par_pagination(donnees_valides, pag=5):
    # pag est le nombre d'éléments à afficher 
    nb_elements = len(donnees_valides)
    nb_pages = (nb_elements + pag - 1) // pag

    for page in range(nb_pages):
        debut = page * pag
        fin = min(debut + pag, nb_elements)
        print(tableau(donnees_valides[debut:fin]))
        print(f"Page {page + 1}/{nb_pages}:")


## Fonction transformation liste en XML
def liste_xml(donnees_valides,chemin_fich_xml):
    # créer l'élément racine
    root = ET.Element("donnees_valides")

    # ajouter les éléments enfants avec les valeurs
    for row in donnees_valides:
        row_elem = ET.SubElement(root, "row")
        for i, value in enumerate(row):
            col_elem = ET.SubElement(row_elem, "col" + str(i))
            col_elem.text = str(value)

    # écrire le fichier XML
    tree = ET.ElementTree(root)
    tree.write(chemin_fich_xml)

    # lire le contenu du fichier et l'afficher
    with open(chemin_fich_xml, 'r') as xml_file:
        content = xml_file.read()
        print(content)



## Fonction transformation liste en JSON
def liste_json(donnees_valides,chemin_fich_json):
    donnees_valides_dict = []
    for row in donnees_valides:
        row_dict = {}
        for i, value in enumerate(row):
            row_dict["col" + str(i)] = value
        donnees_valides_dict.append(row_dict)
    
    # écrire le fichier JSON
    with open(chemin_fich_json, 'w') as json_file:
        json.dump(donnees_valides_dict, json_file, indent=4)
    
    # lire le contenu du fichier et l'afficher
    with open(chemin_fich_json, 'r') as json_file:
       content = json_file.read()
       print(content)
## affichage 
# json_file_path = "Donnees_Projet_Python_DataC5.json"

# liste_json(donnees_valides,json_file_path)

## Fonction transformation liste en CSV
def liste_csv(donnees_valides, chemin_fich_csv):
    # écrire le fichier CSV
    with open(chemin_fich_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for etudiant in donnees_valides:
            writer.writerow(etudiant)

    # lire le contenu du fichier et l'afficher
    with open(chemin_fich_csv, 'r') as csv_file:
        content = csv_file.read()
        print(content)
