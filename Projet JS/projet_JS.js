
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
    var plus = document.createElement("button");
    plus.innerHTML = "+";
    var day = document.createElement("div");
    plus.className = "plus";
    day.className = "day";
    jours.className = "jrs";
    var cours = document.createElement("div");
    // cours.className = "crs" + i;
    cours.setAttribute("class", "crs");
    var emplois = document.createElement("div");
    day.appendChild(jours);
    day.appendChild(plus)
    emplois.appendChild(day);
    emplois.appendChild(cours);
    emplois.setAttribute("class","emplois")
    jours_cours.appendChild(emplois);
    
}
console.log(document.querySelector(".crs:nth-child(1)"))
// const list_enseign = document.getElementById("enseignant");
// const enseign = ['ALy','Mbaye','One','Diouf'];
// for ( i=0 ; i<enseign.length ; i++) {
//     var option = document.createElement("option");
//     option.value="texte";
//     option.textContent = enseign[i];
//     list_enseign.appendChild(option);
// }







