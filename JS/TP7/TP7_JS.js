

const APIURL = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=57'
const IMGPATH = "https://image.tmdb.org/t/p/w1280";
let cont_image = document.getElementById("cont_image");
let section = document.getElementsByTagName("section")

function catologue () {

}

fetch(APIURL)
    .then(function(response){
        return response.json();
    })
    .then(function(donnee){
        
        for (let element of donnee.results) {
            
            // Afficher l'image
            let divImage = document.createElement("div");
            let img = document.createElement("img");
            img.src = `https://image.tmdb.org/t/p/w1280${element.poster_path}`;
            img.alt = "film";
            img.id = "photo"
            // Afficher le titre
            let texte = document.createElement("div");
            texte.id = "texte"
            let titre = document.createElement("div");
            titre.innerHTML = `${element.original_title}`
            // Afficher les votes
            let vote = document.createElement("div")
            vote.innerHTML = `${element.vote_average}`

            divImage.appendChild(img);
            console.log(divImage)
            texte.appendChild(titre);
            texte.appendChild(vote);
            cont_image.appendChild(divImage);
            cont_image.appendChild(texte);
            // section.appendChild(cont_image)
            

            
            
            
        }
    })
