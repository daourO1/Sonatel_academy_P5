j=0
i=0
booleen=True
position=["ADDP","EDDP","SDP","ADDS","EDDS","SDS"]
couleur=['v','j','r','b','c','ro']
while booleen:
    n=int(input("Donner l'ordre de votre matrice carrée: "))
    if n<=4:
        print("L'ordre de matrice doit ètre supérieur à 4.")
    else:
        print("La liste de position: ",position)
        print("La liste de couleur: ",couleur)
        choix=input("Choisisez une position parmi la liste: ")
        while choix not in position:
            choix=input("Invalide.\nChoisisez une autre position: ")
        color=input("Invalide.\nChoisisez une couleur dans la liste: ")
        while color not in couleur:
            if color=='v':
                print("\033[32mv\033[0m")
            elif color=='j':
                print("\033[33mj\033[0m")
            elif color=='r':
                print("\033[31mr\033[0m")
            elif color=='b':
                print("\033[34mb\033[0m")
            elif color=='c':
                print("\033[36mc\033[0m")
            else:
                print("\033[35mro\033[0m")
                break
        matrice=[["x"for i in range(n)]for j in range(n)]
        for i in range(n):
            for j in range(n):
                if choix=='ADDP':
                    if i>j:
                        matrice[i][j] = "\033[34m" + color + "\033[0m"    
                if choix=='EDDP':
                    if i<j:
                        matrice[i][j] = "\033[34m" + color + "\033[0m"  
                if choix=='SDP':
                    if i==j:
                        matrice[i][j] = "\033[34m" + color + "\033[0m"
                if choix=='ADDS':
                    if i+j>n-1:
                        matrice[i][j] = "\033[34m" + color + "\033[0m"                
                if choix=='EDDS':
                    if i+j<n-1:
                        matrice[i][j] = "\033[34m" + color + "\033[0m"                
                if choix=='SDS':
                    if i+j==n-1:
                        matrice[i][j] = "\033[34m" + color + "\033[0m"  
        for row in matrice:
            print("  ".join(row))
    break
                  
                                 
                     