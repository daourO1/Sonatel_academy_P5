phrase=input("Donner une phrase:\n")
lettre_min=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lettre_maj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
code_l=['2','22','222','3','33','333','4','44','444','5','55','555','6','66','666','7','77','777','7777','8','88','888','9','99','999','9999']
chiffre=['0','1','2','3','4','5','6','7','8','9',' ']
code_ch=['a','b','c','d','e','f','g','h','i','j','00']
i=0
j=0
e=0
f=0
phrase_new=[]
phrase_code=[]
for i in range(len(phrase)):
    for j in range(len(lettre_min)):
        if phrase[i]==lettre_min[j]:
            phrase_new.append(code_l[j])
    for e in range(len(lettre_maj)):
        if phrase[i]==lettre_maj[e]:
            phrase_new.append(code_l[e])
    for f in range(len(chiffre)):
        if phrase[i]==chiffre[f]:
            phrase_new.append(code_ch[f])
phrase_code.append(phrase_new[0])
for h in range(1,len(phrase_new)):
    a=phrase_new[h]
    b=phrase_new[h-1]
    if a[0]==b[len(b)-1]:
        phrase_code.append('0')
    phrase_code.append(phrase_new[h])
#print(phrase_code)
#Affichage sans les ''
print("La phrase codée:\n")
for i in phrase_code:
    print(i,end='')

