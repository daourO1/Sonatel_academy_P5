let base = localStorage;

let base_donnee = [];

//donnee JSON
const Enseignant = [
    { idEns: '001', nom:"Aly",modules: ['mod003', 'mod005']},
    { idEns: '002', nom:"Mbaye",modules : ['mod005','mod002']},
    { idEns: '003', nom:"One",modules : ['mod001']}
]

const Salles = [
    { idSalle: 'S1', nomSalle: "Nelson"},
    { idSalle: 'S2', nomSalle: "Mandela"},
    { idSalle: 'S3', nomSalle: "Rose Dieng"}
]

const Classes = [
    { idClass: 'C1', nomClass: "L3 SID"},
    { idClass: 'C2', nomClass: "L3 SID"},
    { idClass: 'C3', nomClass: "L2 MPCI"}
]

const Modules = [
    { idModule: 'mod01', nomModule: "Math"},
    { idModule: 'mod02', nomModule: "Python"},
    { idModule: 'mod03', nomModule: "Algo"},
    { idModule: 'mod04', nomModule: "Analyse"},
    { idModule: 'mod05', nomModule: "Java"}
]

// Stocker les chaînes JSON dans le localStorage
base.setItem('Enseignant',JSON.stringify(Enseignant));
base.setItem('Salles',JSON.stringify(Salles));
base.setItem('Classes',JSON.stringify(Classes));
base.setItem('Modules',JSON.stringify(Modules));

// Récupérer les donnees et convertir les donnees en objet stocker dans base_donnee
const recup_donnee = function (table) {
    let valuesOnTable= base.getItem (table);
    base_donnee = JSON. parse(valuesOnTable);
    return base_donnee;
}

// Récuperer les noms
function recup_element (element,name) {
    let data = base.getItem(element)
    let datas = JSON.parse(data)
    // console.log(datas[name])
    let tab_datas = []
    for (elm in datas) {
        tab_datas.push(datas[elm][name])
    }
    return tab_datas
}

const list_enseign = document.getElementById("enseignant");

let planing = document.getElementById("planing");
let titre = document.getElementsByClassName("titre");
let remplir = document.querySelector("span.remplir")

let enseignant = document.querySelector(".enseignant")
enseignant.addEventListener('click', ()=> {
    enseignant.style.backgroundColor = "#57aedb"
    salle.style.backgroundColor = "#9a9a9a"
    classe.style.backgroundColor = "#9a9a9a"
    module.style.backgroundColor = "#9a9a9a"
    let tableau = recup_element ("Enseignant","nom")
    list_enseign.innerHTML = '';
    for ( i=0 ; i<tableau.length ; i++) {
        var option = document.createElement("option");
        list_enseign.appendChild(option);
        option.textContent = tableau[i];
    }
})

list_enseign.addEventListener('change' ,(event)=> {
    const valeur = event.target.value
    remplir.textContent = valeur;
})

let salle = document.querySelector(".salle")
salle.addEventListener('click', ()=> {
    salle.style.backgroundColor = "#269828"
    classe.style.backgroundColor = "#9a9a9a"
    module.style.backgroundColor = "#9a9a9a"
    enseignant.style.backgroundColor = "#9a9a9a"
    let tableau = recup_element ("Salles","nomSalle")
    list_enseign.innerHTML = '';
    for ( i=0 ; i<tableau.length ; i++) {
        var option = document.createElement("option");
        option.textContent = tableau[i];
        list_enseign.appendChild(option);
    }
})

let classe = document.querySelector(".classe")
classe.addEventListener('click', ()=> {
    classe.style.backgroundColor = "#f78101"
    module.style.backgroundColor = "#9a9a9a"
    enseignant.style.backgroundColor = "#9a9a9a"
    salle.style.backgroundColor = "#9a9a9a"
    let tableau = recup_element ("Classes","nomClass")
    list_enseign.innerHTML = '';
    for ( i=0 ; i<tableau.length ; i++) {
        var option = document.createElement("option");
        option.textContent = tableau[i];
        list_enseign.appendChild(option);
    }
})

let module = document.querySelector(".module")
module.addEventListener('click', ()=> {
    module.style.backgroundColor = "#eb262a"
    enseignant.style.backgroundColor = "#9a9a9a"
    salle.style.backgroundColor = "#9a9a9a"
    classe.style.backgroundColor = "#9a9a9a"
    let tableau = recup_element ("Modules","nomModule")
    list_enseign.innerHTML = '';
    for ( i=0 ; i<tableau.length ; i++) {
        var option = document.createElement("option");
        option.textContent = tableau[i];
        list_enseign.appendChild(option);
    }
})








