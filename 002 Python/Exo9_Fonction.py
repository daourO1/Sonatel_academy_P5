#fonction téléphone
def telephone(tel):
    if len(tel)==9 and tel[:2] in ['77','78','76','75','70','33']:
        return True
    else:
        return False

def operateur(tel):
    if tel.startswith("77") or tel.startswith("78"):
        return "orange"
    elif tel.startswith("70"):
        return "expresso"
    elif tel.startswith("76"):
        return "tigo"
    elif tel.startswith("75"):
        return "promobile"
    else:
        return "opérateur inconnu"


#Fonction menu
def affichage_menu():
    print("1-Afficher les clients de la matrice par opérateurs")
    print("2-Afficher les clients d’un opérateur")
    print("3-Afficher les numéros téléphone d’un client")
    print("4-Modifier ou ajouter un numero telephone pour un client")
    print("5-Sortir")


def modifier_numero(client, nom, prenom, nouveau_tel):
    for i in range(len(client)):
        if client[i][1] == nom and client[i][0] == prenom:
            client[i][2] = nouveau_tel
            return True
    return False