let deplacer = document.getElementById("deplacer")


deplacer.style.backgroundColor="yellow"
deplacer.style.height="75px"
let couleur=""

deplacer.addEventListener("mouseover",function(event){
    event.target.innerHTML="tttttttttttt"
    console.log(event)
    couleur= event.target.style.backgroundColor 
    event.target.style.backgroundColor = "red"
    
})
deplacer.addEventListener("mouseout",function(event){
    event.target.innerHTML=""
   
    event.target.style.backgroundColor = ""
    
})

deplacer.addEventListener("click",function(event){
    alert("Daour")
    
})

