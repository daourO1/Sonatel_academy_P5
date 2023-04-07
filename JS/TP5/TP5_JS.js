const tabQuestion=[
    {
        question: "Quel est le Meilleur Langage de Programmation en 2022",
    a: "Java",
    b: "C",
    c: "Python",
    d: "JavaScript",
    correct: "d"
    },
    {
    question:  "Quelle est la capitale du Sénégal ?",
    a: "Thies",
    b: "Louga",
    c: "Dakar",
    d: "Matam",
    correct: "c"
    },
    {
    question: "Quel est le plus grand pays du monde en superficie ?",
    a: "Russie",
    b: "Chine",
    c: "États-Unis",
    d: "Canada",
    correct: "a"
    },
    {
    question: "Quelle est la capitale de la France ?",
    a: "Berlin",
    b: "Paris",
    c: "Londres",
    d: "Madrid",
    correct: "b"
    }
]

const questions = document.getElementById("questions");
const optionAlabel = document.getElementById("optionAlabel");
const optionBlabel = document.getElementById("optionBlabel");
const optionClabel = document.getElementById("optionClabel");
const optionDlabel = document.getElementById("optionDlabel");
// const submit = document.getElementById("submit");
const result = document.getElementById("result");
const next = document.getElementById("next");
const select = document.getElementsByClassName("select");
var usernameInput = document.querySelector('input');
// var answer = usernameInput.getAttribute('name');
const reponse = document.getElementsByName("answer")
let reponse_final=false



let indice_questionEnCours = 0;
let score = 0;

function afficher_question(){
    const question_actuelle=tabQuestion[indice_questionEnCours];
    questions.textContent = question_actuelle["question"];
    optionAlabel.textContent = question_actuelle["a"];
    optionBlabel.textContent = question_actuelle["b"];
    optionClabel.textContent = question_actuelle["c"];
    optionDlabel.textContent = question_actuelle["d"];
    reponse.forEach(function(i){
        i.checked=false;
        next.disabled=true;
    })
}
afficher_question()

function select_reponse() {
    for (i=0; i<reponse.length; i++) {
        reponse[i].addEventListener('change',(event)=>{
            if (event.target.checked) {
                next.disabled=false;
               
                if (event.target.value === tabQuestion[indice_questionEnCours]["correct"]) {
                    reponse_final=true;
                }
                else {
                    reponse_final=false
                }
            }
        })
        
    }
}
select_reponse()

next.addEventListener('click', (event)=> {
    if (reponse_final===true) {
        score++;
    }
    indice_questionEnCours++;
    if (indice_questionEnCours<tabQuestion.length) {
        afficher_question()
        select_reponse()
        console.log(score)
     
    }  
    if (indice_questionEnCours === tabQuestion.length || reponse_final===true) {
    next.addEventListener('click', (event)=> {
        questions.textContent="Votre score: ${score}/${questions.length}";
    })
}      
})



// function afficher_question_suivant() {
    
    
//     if (indice_questionEnCours === tabQuestion.length) {
        
//     }
//     else {
        
//         next.disabled = true;
//     }
// }





