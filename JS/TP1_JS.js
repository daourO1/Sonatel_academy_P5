// Récupérer le bouton avec l'id "btn_add" dans une variable appelée "btn"
let btn = document.getElementById("btn_add");

// Ajouter un écouteur d'événement "click" sur le bouton et exécuter la fonction "btn_add" lorsque l'événement est déclenché
btn.addEventListener("click", btn_add);

// Définition de la fonction "btn_add"
function btn_add() {
     
  // Créer les éléments HTML
  let divTableau = document.createElement("div"); // Créer un élément "div" et le stocker dans une variable appelée "divTableau"
  divTableau.id = "tableau"; // Définir l'attribut "id" de l'élément "div" créé ci-dessus
  
  let divTeteTab = document.createElement("div"); // Créer un autre élément "div" et le stocker dans une variable appelée "divTeteTab"
  divTeteTab.className = "tete_tab"; // Définir la classe de l'élément "div" créé ci-dessus
  
  let img1 = document.createElement("img"); // Créer un élément "img" et le stocker dans une variable appelée "img1"
  img1.src = "edit-regular-24.png"; // Définir l'attribut "src" de l'élément "img" créé ci-dessus
  img1.alt = "editeur"; // Définir l'attribut "alt" de l'élément "img" créé ci-dessus
  
  let img2 = document.createElement("img"); // Créer un autre élément "img" et le stocker dans une variable appelée "img2"
  img2.src = "trash-regular-24.png"; // Définir l'attribut "src" de l'élément "img" créé ci-dessus
  img2.alt = "corbeille"; // Définir l'attribut "alt" de l'élément "img" créé ci-dessus
  
  let textarea = document.createElement("textarea"); // Créer un élément "textarea" et le stocker dans une variable appelée "textarea"
  //textarea.cols = "40%"; // Définir l'attribut "cols" de l'élément "textarea" créé ci-dessus
  //textarea.rows = "25%"; // Définir l'attribut "rows" de l'élément "textarea" créé ci-dessus
  
  // Ajouter les éléments à la page
  divTableau.appendChild(divTeteTab); // Ajouter l'élément "divTeteTab" créé ci-dessus comme un enfant de l'élément "divTableau"
  divTeteTab.appendChild(img1); // Ajouter l'élément "img1" créé ci-dessus comme un enfant de l'élément "divTeteTab"
  divTeteTab.appendChild(img2); // Ajouter l'élément "img2" créé ci-dessus comme un enfant de l'élément "divTeteTab"
  divTableau.appendChild(textarea); // Ajouter l'élément "textarea" créé ci-dessus comme un enfant de l'élément "divTableau"
  document.body.appendChild(divTableau); // Ajouter l'élé

}