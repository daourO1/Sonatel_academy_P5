
// Selection de les paragraphes HTML
let para = document.getElementsByTagName("p")


//console.log(para[1])

for( i=0; i<para.length; i++) {
    let elet = para[i]
    elet.addEventListener("mouseover",function(event){
        event.target.style.backgroundColor = "blue"
        event.target.style.color = "white"
        event.target.style.cursor = "pointer"
    })
    elet.addEventListener("mouseout",function(event){
        event.target.style.backgroundColor = ""
        event.target.style.color = ""
    })
    elet.addEventListener('click', function(){
        elet.classList.toggle("selected")

    } )
};


// function vers_droite (){
//     let gauche=document.getElementsByClassName("deplacer")
//     let tab=document.getElementsByClassName("tableau")
//     let selection=tab.querySelector(".selected")
//         gauche.appendChild(selection)
// }
// let suivant = document.getElementsByClassName("right")
//     console.log(suivant)
//     suivant.addEventListener('click',vers_droite)

function vers_droite() {
    let gauche = document.getElementsByClassName("deplacer")[0]
    let selection = document.querySelector(".tableau .selected")
    if (selection !== null) {
      gauche.appendChild(selection)
      selection.classList.remove("selected")
    }
  }
  
  let suivant = document.querySelector(".right")
  suivant.addEventListener('click', vers_droite)

  function vers_gauche() {
    let gauche = document.getElementsByClassName("deplacer")[0]
    let selection = document.querySelector(".tableau .selected")
    if (selection !== null) {
      gauche.appendChild(selection)
      selection.classList.remove("selected")
    }
  }
  
  let suivant = document.querySelector(".right")
  suivant.addEventListener('click', vers_droite)