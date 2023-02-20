from datetime import datetime
import re

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
    #if ('A'<=prenom[0]<='Z' or 'a'<=prenom[0]<='z') and len(prenom)>=3 and 'a'<=prenom[1:]<='z':
    import re
    regex_prenom = r'^[A-Za-z][A-Za-z]{2,}$'
    if re.match(regex_prenom, prenom):
        return True
    else:
        return False


## Fonction nom
#nom='sdfg'
def nom_etudiant(nom):
    import re
    regex_nom = r'^[A-Za-z][A-Za-z]{1,}$'
    if re.match(regex_nom, nom):
        return True
    else:
        return False

## Fonction date de naissance
date_naissance='1234'
def date_naissance_etudiant(date_naissance):
    c=['/','-','_',',','|',':','.']
    date=''
    date1=''
    date_naissance1=""
    date_new=""
    new_date=""
    naissance=""
    new_naissance=""
    for i in range(len(date_naissance)):
        if date_naissance[i]==' ' and date_naissance[i+1]==' ':
            continue 
        else:
            date+=date_naissance[i]
    #print(date)
    for i in range(1,len(date)):
        if date[0]==' ' and date[1]==' ':
            continue
        else:
            date1+=date[i]
    #print(date1)
    for i in range(len(date1)):
        if (date1[i] in c and date1[i+1]==' ') or (date1[i] in c and date1[i-1]==' '):
            continue
        else:
            date_new+=date1[i]
    #print(date_new)
    #date1=date_new
    for i in date_new:
        if i!='/' and not i.isalnum():
            new_date=date_new.replace(i,'/')
    # Créer une table de traduction qui remplace tous les caractères de la liste c par /
    table = str.maketrans(dict.fromkeys(c, '/'))
    # Appliquer la table de traduction à la chaîne de caractères new_date
    naissance = new_date.translate(table)
    for i in range(len(naissance)):
        if naissance[i]=='/' and naissance[i+1]=='/':
            continue
        else:
            new_naissance+=naissance[i]
        #return new_naissance
    format_string = "%d/%m/%y"
    try:
        new_naissance=datetime.strptime(new_naissance, format_string)
        return True
    except ValueError:
        return False
veri=date_naissance_etudiant(date_naissance)
print(veri)



# classe='  4  ieme  A'
def classe_etudiant(classe):
    classe1=""
    for i in range(len(classe)):
        if classe[i]==' ':
            continue 
        else:
            classe1+=classe[i]
    print(classe1)
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
    if var[-1] in ['A','B']:
        return True
    else:
        return False
    return var
# veri=classe_etudiant(classe)
# print(veri)

## Fonction note etudiant
#note='Math[12|11:13] #Francais[44|11|8:13] #Anglais[13|11:15] #PC[14:29] #SVT[12|9|16|11:12] #HG[11|10:13]'
def note_etudiant(note):
    if not note:
        return False
    note4 = []
    note1 = note.strip()
    note2 = note1.replace("]", "").replace("|", " ").replace(",", ".")
    note3 = note2.split("#")
    for i in note3:
        matière = i.split("[")
        if len(matière) != 2:
            return False
        note4.append([matière[0].strip(), matière[1].strip()])

    for matière in note4:
        if matière[0].isalpha():
            examens = matière[1].split(':')
            if len(examens) != 2:
                return False
            devoirs = examens[0].split()
            validite_notes = True
            for devoir in devoirs:
                if not (0 <= float(devoir) <= 20):
                    validite_notes = False
            if not (0 <= float(examens[1]) <= 20):
                validite_notes = False
            if not validite_notes:
                return False

    return True
 
def tableau(donnee):
    print(100*'-')
    print("|{0:<20} |{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}".format("Code","Numéro","Nom","Prénom","Date de naissance","Classe","Note"))
    print(100*'-')
    
    print(100*'-')
    for etudiant in donnee:
        code,numero,nom,prenom,date_naissance,classe,note=etudiant
        print("|{0:<20} |{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}".format(
            code,numero,nom,prenom,date_naissance,classe,note
        ))
        
    print(100*'-')
    print()
    print()
    
def tableau1(donnee):
    print(100*'-')
    print("|{0:<20} |{1:<20}|{2:<20}|{3:<20}|{4:<20}|{5:<20}|{6:<20}|{7:<20}".format("Code","Numéro","Nom","Prénom","Date de naissance","Classe","Note","Motif d'invalidité"))
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
    while valeur not in donnee:
        print("Ce numéro n'existe pas dans la base")
        valeur=input("Donner un autre numéro: ")
    for etudiant in donnee:
        if valeur==etudiant[1]:
            var.append(etudiant)
       
    return var

# donnee=[['a','z','e',],['z','r','f','h','k'],['s','f','g','g'],['r','g','j','k','x','s']]

# #fonction affichage 5 premier
# def affichage(donnee):
#     var=[]
#     for i in range(3):
#         for etudiant in donnee:
#             var.append(etudiant)
      
#     return(tableau(var))  
# veri=affichage(donnee)
# print(veri)




