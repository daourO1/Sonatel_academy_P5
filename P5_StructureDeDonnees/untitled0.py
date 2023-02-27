#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:17:17 2023

@author: daour
"""
from datetime import datetime

## Fonction date de naissance
date_naissance=' '
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
    # for i in range(len(date_naissance)):
    #     if date_naissance[i-1]==' ' and date_naissance[i]==' ':
    #         continue 
    #     else:
    #         date+=date_naissance[i]
    # print(date)
    date=date_naissance
    # vérifie si le premier caractère n'est pas un chiffre
    if not date[0].isnumeric() and date!="":  
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
        if naissance[i-1]=='/' and naissance[i]=='/':
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
veri=date_naissance_etudiant(date_naissance)
print(veri)