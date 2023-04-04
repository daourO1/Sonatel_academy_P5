// Récupérer le bouton avec l'id "btn_add" dans une variable appelée "btn"
let btn = document.getElementById("btn_add");

// Ajouter un écouteur d'événement "click" sur le bouton et exécuter la fonction "btn_add" lorsque l'événement est déclenché
btn.addEventListener("click", btn_add);

// Définition de la fonction "btn_add"
function btn_add() {

  // Créer les éléments HTML

  let divTableau = document.createElement("div");
  divTableau.className = "tableau";

  let divTeteTab = document.createElement("div");
  divTeteTab.className = "tete_tab";

  let img1 = document.createElement("img");
  img1.src = "edit-regular-24.png";
  img1.alt = "editeur";
  img1.id = "editeur"

  let img2 = document.createElement("img");
  img2.src = "trash-regular-24.png";
  img2.alt = "corbeille";
  img2.id = "corbeille"

  let textarea = document.createElement("textarea");
  //textarea.cols = "40%"; 
  //textarea.rows = "25%"; 

  // Ajouter les éléments à la page
  divTableau.appendChild(divTeteTab);
  divTeteTab.appendChild(img1);
  divTeteTab.appendChild(img2);
  divTableau.appendChild(textarea);
  document.querySelector(".contener").appendChild(divTableau);

}

// Button suprimer

document.addEventListener("click", function () {
  listTab = document.querySelectorAll(".tableau")
  listTab.forEach(function (element) {
    del = element.querySelector('#corbeille')
    del.addEventListener("click", function () {
      element.remove()
    })
  })
})

// Button éditeur

document.addEventListener("click", function () {
  list = document.querySelectorAll(".tableau")
  list.forEach(function (element) {
    editor = element.querySelector('#editeur')
    editor.addEventListener("click", function () {
      let couleur = document.querySelector("#tete_tab")
      couleur.style.backgroundColor = "pink"
    })
  })
})