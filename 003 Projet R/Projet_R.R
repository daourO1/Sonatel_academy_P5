
donnee = read.csv("Donnees_Projet_Python_DataC5.csv",sep=",",dec=".")
donnee
# Verification numéro
numero_etudiant = function(numero){
  if (numero == "" || is.na(numero)){
    return (F)
  }else{
    if (grepl('^[A-Z0-9]{7}$',numero)){
      return (T)
    }else{
      return (F)
    }
  }
}
# numero_etudiant("AZESQA7")

# Verification nom
nom_etudiant = function(nom){
  if (nom=="" || is.na(nom)){
    return (F)
  }else{
    if (grepl('^[A-Z][A-Za-z ]{1,}$',nom)){
      return (T)
    }else{
      return (F)
    }
  }
    
}
# nom_etudiant('Cyrille  ')

# Verification prenom
prenom_etudiant = function(prenom){
  if ((prenom == "" || is.na(prenom))){
    return (F)
  }else{
    if (grepl('^[A-Za-z][A-Za-z ]{2,}$',prenom)){
      return (T)
    }else{
      return (F)
    }
  }
  
}
# prenom_etudiant("do")

# Verification date de naissance
date_naissance_etudiant = function(date_naissance){
  char=c('/','-','_',',','|',':','.',' ')
  if (is.na(date_naissance)){
    return (F)
  }else{
    # Supprime les espaces unitiles 
    trimws(date_naissance)
    date=gsup(" ","/",date_naissance)
   }
}
date_naissance_etudiant('                        1 fev 2004')
substring("az",1,1)
