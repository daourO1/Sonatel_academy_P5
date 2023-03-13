
donnee = read.csv("Donnees_Projet_Python_DataC5.csv",sep=",",dec=",")
donnee

# Installez d'abord la bibliothèque stringr
# install.packages("stringr")

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
  if (is.na(date_naissance)){
    return (F)
  }else{
    # Supprime les espaces unitiles 
    date_naissance=trimws(date_naissance)
    char = str_detect(date_naissance,'(-)*(,)*(_)*(\\|)*(:)*(\\.)*(;)')
    # Remplacer les caractéres par /
    if (char==T){
      library(stringr)
      date_naissance=str_replace_all(date_naissance, c("-"="/", ","="/", "_"="/", "\\|"="/", ":"="/", "\\."="/", ";"="/"))
     }
    date_naissance = str_replace_all(date_naissance,c('fev'='02',"mars"="3","decembre"="12" ))
    # date_naissance
    # Vérifier si la date est au format jour/mois/année
    # Vérifier si la date est valide
    date_valide = tryCatch(as.Date(date_naissance, format = "%d/%m/%y"), error = function(e) NA)
    # Vérifier si la date est valide ou non
    ifelse(is.na(date_valide), FALSE, TRUE)# date=gsup(" ","/",date_naissance)
    
  }
}
# date_naissance_etudiant('07-06-199Ç')

# Verification de classe
classe_etudiant = function(classe) {
  classe=trimws(classe)
  tryCatch({
    if (is.na(classe) || classe == "") {
      return(FALSE)
    } else {
      # Supprime les espaces et les caractères 
      classe1 <- gsub("[[:space:]|,;.-]+", "", classe)
      
      if (grepl("^[3-6][[:alpha:]]*$", classe1)) {
        # Si la classe commence par 3, 4, 5 ou 6 suivis d'une lettre, alors c'est une classe de collège
        if (substr(classe1, nchar(classe1), nchar(classe1)) %in% c("A", "B")) {
          return(TRUE)
        } else {
          return(FALSE)
        }
      } else {
        # Sinon, ce n'est pas une classe valide
        return(FALSE)
      }
    }
  }, error = function(e) {
    return(FALSE)
  })
}
# classe_etudiant("Tlel'1")
# sapply(note, strsplit(""))

# Verification de note
note_etudiant = function(note){
  if (is.na(note) || note==""){
    return (F)
  }else{
    note=trimws(note)
    note=gsub("]","",note)
    note=strsplit(note,"#")
    for (matiere in note){
      matiere = strsplit(matiere,"\\[")
      # print(matiere)
      # print(matiere[[1]][2])
      for (i in 1:length(matiere)){
        if (grepl("[[:alpha:]]",matiere[[i]][1])){
          notes=strsplit(matiere[[i]][2],":")
          print(notes[[1]])
          if (length(notes[[1]])==2){
            if (notes[[1]][2]<=20){
              # return(T)
              note_dev=strsplit(notes[[1]][1],"\\|")
              # print(note_dev[[1]])
              for (i in range(length(note_dev))){
                if (note_dev[[1]][i]<=20){
                  # print(note_dev[[1]][1])
                  return (T)
                }else{
                  return (F)
                }
              }
            }else{
              return (F)
            }
          }else{
            return (F)
          }
        }else{
          return (F)
        }
        
      }
      # print(matiere)
    }
  }
}
note_etudiant('Math[10|11:15] #Francais[:13] #Anglais[13,5|9:15] #PC[11:9]  #HG[10:13]  #SVT[12|9|16|21:12]')

