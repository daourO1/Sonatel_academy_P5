let lp=document.getElementById("lp")
let lmaj=document.getElementById("lmaj")
let lmin=document.getElementById("lmin")
let nombr=document.getElementById("nombr")
let carspe=document.getElementById("carspe")
const bouton=document.querySelector("button")
const recuperer=document.querySelector("header")

function majuscule(){
    list_lmaj="AZERTUIOPMLKJHGFDSQWXCVBN"
    return list_lmaj[Math.floor(Math.random()*list_lmaj.length)]
}

function minuscule(){
    list_lmin="azertyuiopmlkjhgfdsqwxcvbn"
    return list_lmin[Math.floor(Math.random()*list_lmin.length)]
}

function nombre(){
    list_nombr="0123456789"
    return list_nombr[Math.floor(Math.random()*10)]
}

function caractere(){
    list_carspe=",;:!?./§ù%*µ^$¨£&é-çà=}]@\|^"
    return list_carspe[Math.floor(Math.random()*list_carspe.length)]
}
// console.log(caractere())

const objet={
    Maj:majuscule,
    Min:minuscule,
    number:nombre,
    symbol:caractere
}
function generatePassword(taille, Maj, Min, number, symbol) {
    let mot_de_pas="";
    const ele_cocher=Maj+Min+number+symbol
    const booleen_ele=[{Maj},{Min},{number},{symbol}].filter(indice=>Object.values(indice)[0])
    if (ele_cocher===0){
        return ""
    }
    for (i=0; i<taille;i+=ele_cocher) {
        booleen_ele.forEach(type=>{
            const fn=Object.keys(type)[0]
            mot_de_pas+=objet[fn]()
        })
    }
    const motdepasse_final= mot_de_pas.slice(0,taille)
    return motdepasse_final
}   
bouton.addEventListener('click',()=>{
    const longueur=+lp.value
    const Majuscule=lmaj.checked
    const Minuscule=lmin.checked
    const Nombre=nombr.checked
    const Symbol=carspe.checked

    recuperer.innerText=generatePassword(longueur,Majuscule,Minuscule,Nombre,Symbol)
})
