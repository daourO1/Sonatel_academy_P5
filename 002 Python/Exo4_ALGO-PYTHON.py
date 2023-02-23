## EXERCICE4:
i=0
booleen=True
def numero(st):
    if len(st)==9 and (st[:2]=='77' or st[:2]=='78' or st[:2]=='76' or st[:2]=='75' or st[:2]=='70'):
        print("C'est un bon numero:",st)
        return True
    elif len(st)==9 and (st[:2]!='77' or st[:2]!='78' or st[:2]!='76' or st[:2]!='75' or st[:2]!='70'):
        print("C'est pas un bon numero:",st)
        return False
    else:
        print("C'est pas un bon numero:",st)
    return False
while booleen:
  #  numero="Donner des numeros:\n"
    st=''
    tab=[]
    numero_valide=[]
    numero_invalide=[]
    chaine_new=""
    chaine='77 4454430,7* 45?456,783719445,77 546 45 24 ,77 7152378,- 77675yy,]776'#input(numero)
    for i in range(len(chaine)):
        if '0'<=chaine[i]<='9' or chaine[i]==',':
            chaine_new+=chaine[i]
        else:
            continue
    print(chaine_new)
    for char in chaine_new:
        tab.append(char)
    i=0
    while i < len(tab):
        if tab[i] == ',':
            st = ''
        else:
            st += tab[i]
            if (i + 1 < len(tab) and tab[i + 1] == ',') or i == len(tab) - 1:
                if numero(st):
                    numero_valide.append(st)
                else:
                    numero_invalide.append(st)
        i += 1
    print("Numeros valides: ", numero_valide)
    print("Numeros Invalides: ", numero_invalide)
    break


##    for i in range(len(tab)):
##        st+=tab[i]
##        if tab[i+1]==',':
##            break
##            st=st[i:i-1]
##        i+=1
##    numero(st)
##    break
####    if chaine_new[i;len(chaine_new);10]==',':
####        chaineV+=
####            
    
           
