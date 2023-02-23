
i=0
j=0
booleen=True
while booleen:
    n=int(input("Donner l'ordre de votre matrice: "))
    if n<=5:
        print("L'ordre doit ètre supérieur à 5.")
    else:
        couleur=input("Choisisez entre bleu et rouge: ")
        while couleur not in ["b","r"]:
            couleur=input("Invalide.\nChoisisez entre bleu et rouge: ")
            if couleur=='b':
                print("\033[34mb\033[0m")
            else:
                print("\033[31mr\033[0m")
        position=input("Choisisez une position haut ou bas: ")
        while position not in ["haut","bas"]:
            position=input("Invalide.\nChoisisez une position haut ou bas: ")
        matrice=[["x"for i in range(n)]for j in range(n)]
        for i in range(n):
            for j in range(n):
                if position=='haut':
                    if i<j:
                        if couleur == "b":
                            matrice[i][j] = "\033[34m" + couleur + "\033[0m"
                        else:
                            matrice[i][j] = "\033[31m" + couleur + "\033[0m"
                        #matrice[i][j]=couleur
                        #matrice[i][j] = "\033[31m" + couleur + "\033[0m"

                else:
                    if i>j:
                        if couleur == "b":
                            matrice[i][j] = "\033[34m" + couleur + "\033[0m"
                        else:
                            matrice[i][j] = "\033[31m" + couleur + "\033[0m"
                        #matrice[i][j]=couleur
        for row in matrice:
            print("   ".join(row))
        