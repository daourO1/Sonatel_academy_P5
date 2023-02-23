## EXERCICE2:
cc=(input("Donner une phrase: \n"))

def suprime_espace(cc, var=''):
    cn=''
    i=0
    for i in range(len(cc)):
        if cc[i]==' ' and cc[i+1]==' ':
            continue 
        else:
            cn+=cc[i]
    return cn
cn=suprime_espace(cc,' ')
print ("La phrase correcte est: \n",cn)
