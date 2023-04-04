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
    },
    {
    question: "Combien de planètes composent le système solaire ?",
    a: "8",
    b: "9",
    c: "10",
    d: "7",
    correct: "a"
    }
]

const question = document.getElementById("question");
const optionA = document.getElementById("optionA");
const optionB = document.getElementById("optionB");
const optionC = document.getElementById("optionC");
const optionD = document.getElementById("optionD");
const submit = document.getElementById("submit");
const result = document.getElementById("result");
const next = document.getElementById("next");

let indice_questionEnCours = 0;
let score = 0;

function afficher_question(){
    const question_actuelle=tabQuestion[indice_questionEnCours];
    question.textContent = question_actuelle.question;
    optionA.textContent = question_actuelle.a;
    optionB.textContent = question_actuelle.b;
    optionC.textContent = question_actuelle.c;
    optionD.textContent = question_actuelle.d;
    submit.disabled = true;
    next.disabled = true;
}

function selection_reponse(event) {
    const select = event.target.value;
    if (select === tabQuestion[indice_questionEnCours].correct) {
        score++;
    }
    next.disabled = false;
    next.addEventListener('click',)
}

function afficher_question_suivant() {
    indice_questionEnCours++;
    if (indice_questionEnCours>=tabQuestion[indice_questionEnCours]) {
        
    }
}
// tabQuestion.forEach(element=>{
//     // console.log(element['question'])
//     let h1=document.createElement("h1")
//     h1.textContent=element['question']
// })




