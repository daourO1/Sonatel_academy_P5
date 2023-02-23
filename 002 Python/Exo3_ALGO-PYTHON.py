##EXERCICE3:
#texte=chaine
booleen = True
message = "Entrez un texte: \n"
while booleen:
    chaine = input(message)
    chaine_new = ""
    phrase = ""
    i = 0
    while i < len(chaine):
        if chaine[i] != " " or (chaine[i] == " " and chaine[i-1] != " "):
            phrase += chaine[i]
        
        if i+1 < len(chaine) and (chaine[i] == "." or chaine[i] == "!" or chaine[i] == "?"):
            if 65 <= ord(phrase[0]) <= 90:
                if len(phrase) < 25:
                    message = "Vos phrases doivent avoir au moins 25 caractères."
                    break
                for j in range(len(phrase)):
                    if 65 <= ord(phrase[j]) <= 90 or 97 <= ord(phrase[j]) <= 122 or 48 <= ord(phrase[j]) <= 57 or phrase[j] == " " or ord(phrase[j]) == 39:
                        chaine_new += phrase[j]
                    else:
                        message = "Vos phrases contiennent des caractères spéciaux ou ne terminent pas par la ponctuation autorisée."
                        break
                chaine_new += chaine[i]
                phrase = ""
            else:
                message = "Vos phrases ne commencent pas par des majuscules."
                break
        i += 1

    if chaine_new == chaine:
        booleen = False

print("Le texte est:", chaine_new)
