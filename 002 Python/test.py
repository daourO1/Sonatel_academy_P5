####EXERCICE1
##print ("Le menu de choix est la suivante: \n 1. Mois en Fran√ßais \n 2. Mois en Anglais \n 3. Quitter")
##tab_f=["Janvier","F√©vrier","Mars","Avril","Mai","Juin","Juillet","Ao√ªt","Septembre","Octobre","Novembre","D√©cembre"]
##tab_a=["January","February","March","April","May","June","July","August","September","October","November","December"]
##i=0
##j=0
##n=int(input("Vous choisisez: "))
##if n==1 or n==2:
##    if n==1:
##        tab = tab_f
##    else:
##         tab = tab_a
##    for j in range(3)
##        for i in range(j,12,3):
##            if len(tab[i])<10:
##                tab[i]+=(10-len(tab[i]))*' '
##            print (tab[i],end='| ')
##        print ('\n')
##elif n==3:
##    print ("Quitter")
##else:
##    print ("On a que 3 choix disponible.")
##
##
#### EXERCICE3:
##import re
##booleen=False
##Chaine_new=''
##i=0
##j=0
####motif=r"^[A-Z][A-Za-z\s]+[.?!]$"
##while (booleen==False):
##    n=int(input("Donner le nombre de phrases que vous voulez mettre dans la chaine: "))
##    chaine=[input("Phrase : ") for i in range(n)]
##    print (chaine)
##    for i in range(n):
##        if len(chaine[i])>=25 and re.match("^[A-Z][A-Za-z0-9\s]*[\.\?!]$", chaine[i]):
##            for j in range(len(chaine)):
##                if chaine[j]==' ' and chaine[j+1]==' ':
##                    continue 
##                else:
##                    Chaine_new+=chaine[j]
##            print ("On a cette nouveau chaine: ",Chaine_new)
##            booleen=True
##        else:
##            print ("La chaine est invalide")
##            booleen=False
##
##
##r"^[A-Z][A-Za-z0-9\s]+[.?!]$"
##
##
#### la fonction 'is_valid_sentence()' utilise 're.match()' pour v√©rifier si
#### la cha√Æne 'sentence' correspond √  l'expression r√©guli√®re 'pattern'.
#### Le motif d√©fini avec 'pattern' :
#### Commence par une majuscule ('^[A-Z]')
#### Contient ensuite un ou plusieurs caract√®res alphanum√©riques ou des espaces ('[A-Za-z\s]+')
#### Se termine par un point, un point d'interrogation ou un point d'exclamation ('[.?!]$')
#### Si une correspondance est trouv√©e, la fonction renvoie 'True', sinon elle renvoie 'False'.
##
##
####L'expression r√©guli√®re pattern est d√©finie comme suit :
####
####^ : d√©but de la cha√Æne
####[A-Z] : une seule lettre majuscule
####[A-Za-z\s]+ : un ou plusieurs caract√®res alphanum√©riques ou espaces
####[.?!] : un seul point, point d'interrogation ou point d'exclamation
####$ : fin de la cha√Æne
####L'expression r√©guli√®re correspond donc √  une cha√Æne qui commence par une majuscule, suivie d'un ou plusieurs caract√®res alphanum√©riques ou espaces, et se termine par un point, un point d'interrogation ou un point d'exclamation.
##
# |Pr√©nom       |Nom         |Classe      |T√©l√©phone   |Devoir      |Projet      |Examen      |Moyenne     
# ----------------------------------------------------------------------------------------------------------------
# |Daour        |Ndaw        |Cm          |774453330   |12.00       |11.00       |10.00       |11.00       
# |Mouhamed     |THiam       |L           |774453354   |9.00        |8.00        |12.00       |9.67        
# |Serigne      |NDAW        |Sd          |762331289   |12.00       |16.00       |9.00        |12.33       
# ------------------------------------------------------------------------------------------------------------
# etudiant=[["Daour","Ndaw","Cm","774453330","12.00","11.00","10.00","11.00"],["Mouhamed","THiam","L","774453354","9.00","8.00","12.00","9.67"]]
# etudiant=[12,20,15,18,18]
# def trie_etudiant(etudiant):
#     for i in range(len(etudiant) - 1):
#         elm1=i
#         for j in range(i + 1, len(etudiant)):
#             if etudiant[i] < etudiant[j]:
#                 elm1=j
#                 etudiant[i], etudiant[elm1] = etudiant[elm1], etudiant[i]           
#     return etudiant
# tab=trie_etudiant(etudiant)
# print(tab)



# Programme EXO6.txt
# Affichage de Programme EXO6.txt
# note='[12|11:13] #Francais[14|11|8:13,5] #Anglais[13|11:15] #PC[:19] #SVT[12|9|16|11:12] #HG[11|10:13]'

# def note_etudiant(note):
#     if not note:
#         return False
#     note4 = []
#     note1 = note.strip()
#     note2 = note1.replace("]", "").replace("|", " ").replace(",",".")
#     note3 = note2.split("#")
#     for i in note3:
#         matiËre = i.split("[")
#         note4.append([matiËre[0].strip(), matiËre[1].strip()])

#     for matiËre in note4:
#         if len(matiËre)==2:
#             if matiËre[0].isalpha():
#                 examens = matiËre[1].split(':')
#                 if len(examens)==2:
#                     devoirs = examens[0].split()
#                     validite_notes = True
#                     for devoir in devoirs:
#                         if not (0 <= float(devoir) <= 20):
#                             validite_notes = False
#                     if not (0 <= float(examens[1]) <= 20):
#                         validite_notes = False
#                     if not validite_notes:
#                         return False

#     return True

# veri=note_etudiant(note)
# print(veri)


note='PC[17|20|18:15]#Math[15|16,15|13:17]#Francais[11:13]#Anglais[14:13]#SVT[13|11|15|11:12]#HG[15:13]'
def note_etudiant(note):
    if not note:
        return False
    note4 = []
    note1 = note.strip()
    note2 = note1.replace("]", "").replace("|", " ").replace(",", ".")
    note3 = note2.split("#")
    for i in note3:
        matiËre = i.split("[")
        if len(matiËre) != 2:
            return False
        note4.append([matiËre[0].strip(), matiËre[1].strip()])

    for matiËre in note4:
        if matiËre[0].isalpha():
            examens = matiËre[1].split(':')
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
veri=note_etudiant(note)
print(veri)