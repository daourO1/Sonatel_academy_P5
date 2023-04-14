let base = localStorage;

let base_donnee = [];

//donnee JSON
const Enseignant = [
    { idEns: '001', nom:"Aly",modules: ['mod003', 'mod005']},
    { idEns: '002', nom:"Mbaye",modules : ['mod005','mod002']},
    { idEns: '003', nom:"One",modules : ['mod001']}
]

const Salles = [
    { idSalle: 'S1', nomSalle: "Nelson", effSalle: "30"},
    { idSalle: 'S2', nomSalle: "Mandela", effSalle: "40"},
    { idSalle: 'S3', nomSalle: "Rose Dieng", effSalle: "50"}
]

const Classes = [
    { idClass: 'C1', nomClass: "L3 SID", effClass: "29"},
    { idClass: 'C2', nomClass: "L3 SID", effClass: "40"},
    { idClass: 'C3', nomClass: "L2 MPCI", effClass: "60"}
]

const Modules = [
    { idModule: 'mod01', nomModule: "Math"},
    { idModule: 'mod02', nomModule: "Python"},
    { idModule: 'mod03', nomModule: "Algo"},
    { idModule: 'mod04', nomModule: "Analyse"},
    { idModule: 'mod05', nomModule: "Java"}
]

const Heures = [
    {h: '8'},{h: '9'},{h: '10'},{h: '11'},{h: '12'},{h: '13'},{h: '14'},{h: '15'},{h: '16'},{h: '17'}
]

const Cours = [
    {nomModule: "", nom: "", nomSalle: '', nomClass: "", hDebut: "", hFin: "",}
]

// const link = [
//     {nom: "" },
//     {nomSalle: "" },
//     {nomClass: "" },
//     {nomModule: "" }
// ]

// Stocker les chaînes JSON dans le localStorage
base.setItem('Enseignant',JSON.stringify(Enseignant));
base.setItem('Salles',JSON.stringify(Salles));
base.setItem('Classes',JSON.stringify(Classes));
base.setItem('Modules',JSON.stringify(Modules));
base.setItem('Heures',JSON.stringify(Heures));


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
    var zone_text = document.createElement('option');
    zone_text.textContent = "~~Enseignant~~";
    list_enseign.appendChild(zone_text);
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
    zone_text.textContent = "~~Salle~~";
    list_enseign.appendChild(zone_text);
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
    zone_text.textContent = "~~Classe~~";
    list_enseign.appendChild(zone_text);
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
    zone_text.textContent = "~~Module~~";
    list_enseign.appendChild(zone_text);
    for ( i=0 ; i<tableau.length ; i++) {
        var option = document.createElement("option");
        option.textContent = tableau[i];
        list_enseign.appendChild(option);
    }
})

let next = document.querySelector("#next");
let trello = document.querySelector("#trello");
let partie2 = document.querySelector("#partie2");
let jrs = document.querySelector(".jrs");
let crs = document.querySelector(".crs");
next.addEventListener('click', ()=> {
    trello.style.backgroundColor = "#b7c3cc";
    partie2.style.backgroundColor = '#efafb0';
    jrs.style.backgroundColor = "#ed9b9e";
    crs.style.backgroundColor = "#c0bfc6";
})

// Ajout element dans emplois du temps
let addition = document.querySelectorAll('.plus');
let dialogue = document.querySelector('dialog')
let choix_module = document.querySelector("#choix_module");
let choix_enseign = document.querySelector("#choix_enseign");
let choix_salle = document.querySelector("#choix_salle");
let hDebut = document.querySelector("#hDebut");
let hFin = document.querySelector("#hFin");
let j = document.querySelector(".j")

addition.forEach((element,i) => {

    element.addEventListener('click', ()=> {
        j.innerHTML = tabJours[i];
        dialogue.showModal();
        let tableau = recup_element ("Modules","nomModule")
        choix_module.innerHTML = '';
        var zone_text = document.createElement('option');
        zone_text.textContent = "Choisir un module";
        choix_module.appendChild(zone_text);
        for ( i=0 ; i<tableau.length ; i++) {
            var option = document.createElement("option");
            option.textContent = tableau[i];
            choix_module.appendChild(option);
        }
        let tableau2 = recup_element ("Enseignant","nom")
        choix_enseign.innerHTML = '';
        var zone_text = document.createElement('option');
        zone_text.textContent = "Choisir un Enseignant";
        choix_enseign.appendChild(zone_text);
        for ( i=0 ; i<tableau2.length ; i++) {
            var option = document.createElement("option");
            option.textContent = tableau2[i];
            choix_enseign.appendChild(option);
        }
        let tableau1 = recup_element ("Salles","effSalle")
        choix_salle.innerHTML = '';
        var zone_text = document.createElement('option');
        zone_text.textContent = "Choisir une Salle";
        choix_salle.appendChild(zone_text);
        for ( i=0 ; i<tableau1.length ; i++) {
            var option = document.createElement("option");
            option.textContent = tableau1[i];
            choix_salle.appendChild(option);
        }
        let tableau3 = recup_element ("Heures","h")
        hDebut.innerHTML = '';
        var zone_text = document.createElement('option');
        zone_text.textContent = "Choisir une Heure";
        hDebut.appendChild(zone_text);
        for ( i=0 ; i<tableau.length ; i++) {
            var option = document.createElement("option");
            option.textContent = tableau3[i];
            hDebut.appendChild(option);
        }
        let tableau4 = recup_element ("Heures","h")
        hFin.innerHTML = '';
        var zone_text = document.createElement('option');
        zone_text.textContent = "Choisir une Heure";
        hFin.appendChild(zone_text);
        for ( i=0 ; i<tableau.length ; i++) {
            var option = document.createElement("option");
            option.textContent = tableau4[i];
            hFin.appendChild(option);
        }
    })
    
});

// Cliquer sur annuler pour fermer la boite de dialogue
let annul = document.querySelector(".annul");
annul.addEventListener('click', ()=> {
    dialogue.close();
})


// Ajouter dans emplois du temps

choix_module.addEventListener('change' ,(event)=> {
    const valeur = event.target.value;
    Cours.nomModule = valeur;
})
choix_enseign.addEventListener('change' ,(event)=> {
    const valeur1 = event.target.value;
    Cours.nom = valeur1;
})
choix_salle.addEventListener('change' ,(event)=> {
    const valeur2 = event.target.value;
    Cours.effSalle = valeur2;
})
hDebut.addEventListener('change' ,(event)=> {
    const valeur3 = event.target.value;
    Cours.hDebut = valeur3;
})
hFin.addEventListener('change' ,(event)=> {
    const valeur4 = event.target.value;
    Cours.hFin = valeur4;
})

let ajout = document.querySelector(".ajout");
ajout.addEventListener('click', ()=> {
    let add = document.createElement("div");
    add.className = "add";
    var valE = document.createElement("p");
    valE.className = "valE"
    const valE1 = document.createTextNode(Cours.nom);
    valE.appendChild(valE1);
    add.appendChild(valE);
    var valM = document.createElement("h1");
    const valM1 = document.createTextNode(Cours.nomModule);
    valM.appendChild(valM1);
    add.appendChild(valM);
    var valS = document.createElement("p");
    const valS1 = document.createTextNode(Cours.effSalle);
    valS.appendChild(valS1);
    add.appendChild(valS);
    a =document.querySelector('.j').textContent
    pos = tabJours.indexOf(a)+1
    // console.log(pos)
    crs=document.querySelector(`.emplois:nth-child(${pos}) > .crs`)
    crs.appendChild(add);
    dialogue.close();
})
// let programme = document.createElement("div")
// var valM = 
