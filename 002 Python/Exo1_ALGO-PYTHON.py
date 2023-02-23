## EXERCICE1:
tab_f=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
tab_a=["January","February","March","April","May","June","July","August","September","October","November","December"]
i=0
j=0
booleen=True
while (booleen):
    print ("Le menu de choix est la suivante: \n 1. Mois en Français \n 2. Mois en Anglais \n 3. Quitter")
    n=int(input("Vous choisisez: "))
    if n==1 or n==2 or n==3:
        booleen=False
if n==1 or n==2:
    if n==1:
        tab = tab_f
    else:
         tab = tab_a
    for j in range(3):
        for i in range(j,12,3):
            if len(tab[i])<10:
                tab[i]+=(10-len(tab[i]))*' '
            print (tab[i],end='| ')
        print ('\n')
elif n==3:
    print ("Quitter")
else:
    print ("On a que 3 choix disponible.")


