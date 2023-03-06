from datetime import datetime
import re
import json
import xml.etree.ElementTree as ET
import csv

class transformation_csv:
    def csv_json(self):
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
        # ouvrir le fichier JSON en mode écriture
        with open(chemin_fich_json, 'w') as json_file:
            # écrire les données au format JSON dans le fichier
            dataJ=json.dumps(donneesJ)
            json_file.write(dataJ)
            dataJ=json.loads(dataJ)
        return dataJ
# tab=[]
# t=transformation()
# tab=t.csv_json()
# print(tab)
    def csv_xml(self):
        #nom du fichier CSV à lire
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
                xml_file.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no'?>\n<Etudiants>")
                
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
                xml_file.write("\n</Etudiants>")
                #print("Les données XML: \n",donneeX)

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
                    # print(element)
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
        return donneesX
# tab=[]
# t=transformation()
# tab=t.csv_xml()
# print(tab)
class affichage:
    def __init__(self,optionJ,optionX):
        self.optionsJ = [
            "Transformation données valides JSON en XML ",
            "Transformation données valides JSON en CSV ",
            "Transformation données invalides JSON en XML",
            "Transformation données invalides JSON en CSV",
            ]
        self.optionsX = [
            "Transformation données valides XML en JSON ",
            "Transformation données valides XML en CSV ",
            "Transformation données invalides XML en CSV",
            "Transformation données invalides XML en JSON",
            ]
    def en_tete(self):
        print()
        print(100*'-')
        print(30*' ',"⏩ ⏩ ⏩ ⏩ ⏩   MENU   ⏪ ⏪ ⏪ ⏪ ⏪ ")
        print(100*'-')
    def affichage_menuJ(self):
            for i, optionJ in enumerate(self.optionsJ, 1):
                print(f"   {i}- {optionJ}")
    def affichage_menuX(self):
            for i, optionX in enumerate(self.optionsX, 1):
                print(f"   {i}- {optionX}")
# menu = affichage("option")
# menu.affichage_menu()

class verification:
    def __init__(self,numero,nom,prenom,date_naissance,classe,note):
        self.numero=numero
        self.nom=nom
        self.prenom=prenom
        self.date_naissance=date_naissance
        self.classe=classe
        self.note=note
    ## Fontion pour les numéros
    def numero_etudiant(self,numero):
        if not numero:
            return False
        # Vérifier si le numéro est valide en utilisant l'expression régulière
        regex = r'^[A-Z0-9]{7}$'
        if re.match(regex, numero):
            return True
        else:
            return False
    ## Fonction nom
    def nom_etudiant(self,nom):
        if not nom:
            return False
        regex_nom = r'^[A-Z][A-Za-z ]{1,}$'
        if re.match(regex_nom, nom):
            return True
        else:
            return False
    ## Fonction prénom
    def prenom_etudiant(self,prenom):
        if not prenom:
            return False
        regex_prenom = r'^[A-Za-z][A-Za-z ]{2,}$'
        if re.match(regex_prenom, prenom):
            return True
        else:
            return False
    ## Fonction date de naissance
    def date_naissance_etudiant(self,date_naissance):
        if date_naissance!="":
            # return False
            c=['/','-','_',',','|',':','.',' ']
            date=''
            date1=''
            date_naissance1=""
            date_new=""
            new_date=""
            naissance=""
            new_naissance=""
            # Supprime les espace inutiles
            for i in range(len(date_naissance)-1):
                if date_naissance[i]==' ' and date_naissance[i+1]==' ':
                    continue 
                else:
                    date+=date_naissance[i]
            # print(date)
            date=date_naissance
            # vérifie si le premier caractère n'est pas un chiffre
            if not date[0].isnumeric() and date!="":  
                # supprime le premier caractère de la chaîne
                date_new = date[1:]  
            else:
                date_new=date
            # print(date_new)
            # Créer une table de traduction qui remplace tous les caractères de la liste c par /
            table = str.maketrans(dict.fromkeys(c, '/'))
            # Appliquer la table de traduction à la chaîne de caractères new_date
            naissance = date_new.translate(table)
            # print(naissance)
            # Supprime les '/' inutiles
            for i in range(len(naissance)-1):
                if naissance[i]=='/' and naissance[i+1]=='/':
                    continue
                else:
                    new_naissance+=naissance[i]
                # if new_naissance[-1]=="/":
                #     del(new_naissance[-1])
            # print(new_naissance)
            # Verifier si la date respecte le format jour/mois/année
            format_string = "%d/%m/%y"
            try:
                new_naissance=datetime.strptime(new_naissance, format_string)
                return True
            except ValueError:
                return False
        
    def classe_etudiant(self,classe):
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
    ## Fonction note etudiant
    def note_etudiant(self,note):
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
    # Fonction Calcul moyen


class note_moyenne:
    def __init__(self,note,donnees_valides):
        self.note=note
        self.donnees_valides=donnees_valides
    def moyenne(self,note):
        note1 = self.note.strip()
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
        
        try:
            moyenne_G = moy_G / len(note4) 
            moyenne_G = round(moyenne_G, 3)
            # print(moyenne_G)
            return moyenne_G
        except Exception:
            pass
        
    def remplacer_notes_par_moyennes(self,donnees_valides):
        new_donnees_valides = []
        for etudiant in self.donnees_valides:
            # code,numero,nom,prenom,date_naissance,classe,note=etudiant
            
            d=note_moyenne(self.note,self.donnees_valides)
            moyenne_generale = d.moyenne(self.note)
            etudiant["Moyenne Générale"]=moyenne_generale
            # etudiant.pop("Note")
            # print(etudiant)
            # etudiant.append(etudiant["Moyenne Générale"])
            new_donnees_valides.append(etudiant)
        return new_donnees_valides



    


# #note='Math[10|11:15] #Francais[7|12|8:13] #Anglais[13,5|9:15] #PC[11:9]  #SVT[12|9|16|11:12]  #HG[10:13]'
    
#     # for etudiant in donnees_valides:
#     #     code,numero,nom,prenom,date_naissance,classe,note=etudiant
#     #     etudiant.remove(note)
#     #     etudiant.append(moy_G)
#     # new_donnees_valides.append(etudiant)
        
            
#     #         examens.append(moy_G)
#     #         #print(moy_G)
#     #         matières[matière[0]]=examens
#     # note5.append(matières)
    
#     #print(note5)
            
#             #for devoir in devoirs:
                
#             # if not (0 <= float(examens[1]) <= 20):
#             #     validite_notes = False
#             # if not validite_notes:
#             #     return False
#     #return moy_G
# # veri=moyenne(note)
# # print(veri)


 
# def tableau(donnee):
#     print(140*'-')
#     print("|{0:<20}|{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}".format("Code","Numéro","Nom","Prénom","Date de naissance","Classe","Moyenne Etudiant"))
#     print(140*'-')
    
#     for etudiant in donnee:
#         code,numero,nom,prenom,date_naissance,classe,note=etudiant
#         print("|{0:<20}|{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}".format(
#             code,numero,nom,prenom,date_naissance,classe,note
#         ))
        
#     print(140*'-')
#     print()
#     print()
    
# def tableau1(donnee):
#     print(100*'-')
#     print("|{0:<20} |{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}|{7:<20}|{8:<20}".format("Code","Numéro","Nom","Prénom","Date de naissance","Classe","Note","Motif d'invalidité"))
#     print(100*'-')
    
#     print(100*'-')
#     for etudiant in donnee:
#         code,numero,nom,prenom,date_naissance,classe,note,motif=etudiant
#         print("|{0:<20} |{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}|{7:<20}".format(
#             code,numero,nom,prenom,date_naissance,classe,note,motif
#         ))
        
#     print(100*'-')
#     print()
#     print()


# #fonction recherche
# def recherche(valeur,donnee):
#     var=[]
#     #veri=numero_etudiant(valeur)
#     for etudiant in donnee:
        
#         while valeur not in etudiant:
#             print("Ce numéro n'existe pas dans la base")
#             valeur=input("Donner un autre numéro: ")
#         # for etudiant in donnee:
#             if valeur==etudiant[1]:
#                 var.append(etudiant)
       
#     return var

# ## Fonction trie
# def trie_etudiant(donnees_valides):
#     for i in range(len(donnees_valides) - 1):
#         for j in range(i + 1, len(donnees_valides)):
#             if donnees_valides[i][6]< donnees_valides[j][6]:
#                 donnees_valides[i], donnees_valides[j] = donnees_valides[j], donnees_valides[i]           
#     return donnees_valides





class transformation:
    ## Fonction transformation liste en XML
    def liste_xml(self,donnees_valides,chemin_fich_xml):
        with open(chemin_fich_xml, 'w') as xml_file:
            xml_file.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no'?>\n<Etudiants>")
            
            donneeX=""
            for etudiant in donnees_valides:
                
                dataX='''
                <etudiant>
                        <CODE> %s </CODE>
                        <Numero> %s </Numero>
                        <Nom> %s </Nom>
                        <Prenom> %s </Prenom>
                        <Date_de_naissance> %s </Date_de_naissance>
                        <Classe> %s </Classe>
                        <Moyenne Generale> %s </Moyenne Generale> 
                </etudiant>''' %(etudiant["CODE"],etudiant["Numero"],etudiant["Nom"],etudiant["Prénom"],etudiant["Date de naissance"],etudiant["Classe"],etudiant["Moyenne Generale"])
                donneeX+=dataX
                
                # écrire les données XML dans un fichier
            xml_file.write(donneeX)
            xml_file.write("\n</Etudiants>")
            #print("Les données XML: \n",donneeX)

    ## Fonction transformation liste en XML
    def liste_xmlI(self,donnees_valides,chemin_fich_xml):
        with open(chemin_fich_xml, 'w') as xml_file:
            xml_file.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no'?>\n<Etudiants>")
            
            donneeX=""
            for etudiant in donnees_valides:
                
                dataX='''
                <etudiant>
                        <CODE> %s </CODE>
                        <Numero> %s </Numero>
                        <Nom> %s </Nom>
                        <Prenom> %s </Prenom>
                        <Date_de_naissance> %s </Date_de_naissance>
                        <Classe> %s </Classe>
                        <Note> %s </Note> 
                </etudiant>''' %(etudiant["CODE"],etudiant["Numero"],etudiant["Nom"],etudiant["Prénom"],etudiant["Date de naissance"],etudiant["Classe"],etudiant["Moyenne Generale"])
                donneeX+=dataX
                
                # écrire les données XML dans un fichier
            xml_file.write(donneeX)
            xml_file.write("\n</Etudiants>")
            #print("Les données XML: \n",donneeX)
            
            
    ## Fonction transformation liste en JSON
    def liste_json(self,donnees_valides,chemin_fich_json):
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
    def liste_csv(self,donnees_valides, chemin_fich_csv):
        # Récupérer les clés de tous les dictionnaires dans la liste
       field_names = set().union(*donnees_valides)
    
       with open(chemin_fich_csv, mode='w', newline='') as csv_file:
           writer = csv.DictWriter(csv_file, fieldnames=field_names)
           writer.writeheader()  # Écrire les noms des colonnes dans le fichier CSV
    
           # Écrire chaque dictionnaire dans la liste en tant que ligne dans le fichier CSV
           for etudiant in donnees_valides:
               writer.writerow(etudiant)
        # # écrire le fichier CSV
        # with open(chemin_fich_csv, 'w', newline='') as csv_file:
        #     writer = csv.writer(csv_file)
        #     for etudiant in donnees_valides:
        #         writer.writerow(etudiant)
    
        # # lire le contenu du fichier et l'afficher
        # with open(chemin_fich_csv, 'r') as csv_file:
        #     content = csv.DictReader(csv_file)
        #     print(content)
            
            
            
            # with open(chemin_fich_csv, 'r') as csv_file:
            #     # créer un lecteur CSV
            #     csv_reader = csv.DictReader(csv_file)
            #     # initialiser une liste pour stocker les données
            #     donneesJ = []
            #     # parcourir les lignes du fichier CSV
            #     for row in csv_reader:
            #         # ajouter la ligne à la liste des données
            #         donneesJ.append(row)
            # # ouvrir le fichier JSON en mode écriture
            # with open(chemin_fich_json, 'w') as json_file:
            #     # écrire les données au format JSON dans le fichier
            #     dataJ=json.dumps(donneesJ)
            #     json_file.write(dataJ)
            #     dataJ=json.loads(dataJ)
            # return dataJ
            
            
    def listeI_xml(self,donnees_invalides,chemin_fich_xml):
        with open(chemin_fich_xml, 'w') as xml_file:
            xml_file.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no'?>\n<Etudiants>")
            
            donneeX=""
            for etudiant in donnees_invalides:
                
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
            xml_file.write("\n</Etudiants>")