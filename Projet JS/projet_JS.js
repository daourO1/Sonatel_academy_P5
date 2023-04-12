
const tabJours = [
    "LUNDI",
    "MARDI",
    "MERCREDI",
    "JEUDI",
    "VENDREDI",
    "SAMEDI"
]
    
const jours_cours = document.getElementById("jours_cours");
for (var jour in tabJours) {
    var jours = document.createElement("div");
    jours.innerHTML = tabJours[jour];
    jours.className = "jrs";
    var cours = document.createElement("div");
    cours.className = "crs";
    var emplois = document.createElement("div");
    emplois.appendChild(jours);
    emplois.appendChild(cours);
    emplois.id = "emplois"
    jours_cours.appendChild(emplois);
    
    
}
// const list_enseign = document.getElementById("enseignant");
// const enseign = ['ALy','Mbaye','One','Diouf'];
// for ( i=0 ; i<enseign.length ; i++) {
//     var option = document.createElement("option");
//     option.value="texte";
//     option.textContent = enseign[i];
//     list_enseign.appendChild(option);
// }







