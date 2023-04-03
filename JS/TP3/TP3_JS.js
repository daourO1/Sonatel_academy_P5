let div_parent = document.getElementById("notification")
let div_enfants = div_parent.querySelectorAll("div")
let projet = document.getElementsByClassName("projet")[0]
// console.log(projet[0])
for (i=0; i<div_enfants.length; i++ ){
  var div_enfant=div_enfants[i];
  div_enfant.addEventListener("click",(event)=>{
    var style = window.getComputedStyle(event.target);
    var couleur = style.getPropertyValue("background-color")
    console.log(couleur)
    projet.style.backgroundColor=couleur
    // switch (couleur) {
    //   case "rgb(55, 140, 55)":
    //     projet.style.backgroundColor="rgb(55, 140, 55)"
    //       break;
    //   case "rgb(55, 140, 55)":
    //     projet.style.backgroundColor="rgb(55, 140, 55)"
    //       break;
      
    // }
  })
  // setTimeout(function() {
  //   // projet.style.backgroundColor="transparent"
  //   projet.style.display = "none"
  // }, 1000);
}