const targetDate = new Date("January 1, 2024 00:00:00");

const jours = document.getElementById("jours")
const heures = document.getElementById("heures")
const minutes = document.getElementById("minutes")
const secondes = document.getElementById("secondes")

function mettre_a_jours_compte() {

    const durée_restant = targetDate - new Date()
    const jours_restant = Math.floor (durée_restant / (1000 * 60 * 60 * 24));
    const heures_restant = Math.floor((durée_restant / (1000 * 60 * 60)) % 24);
    const minutes_retant = Math.floor((durée_restant / 1000 / 60) % 60);
    const secondes_restant = Math.floor((durée_restant / 1000) % 60);
  
    // Mettre à jour l'affichage du compte à rebours
    jours.textContent = jours_restant;
    heures.textContent = heures_restant;
    minutes.textContent = minutes_retant;
    secondes.textContent = secondes_restant;
  }
  
  // Mettre à jour le compte à rebours toutes les secondes
  setInterval(mettre_a_jours_compte, 1000);


