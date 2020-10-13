
displayScore();

function displayScore(){
  let initScore = document.forms["updateScoreForm"].elements[1].value;
  document.getElementById("score").textContent = initScore;
}

function setScore(){
  displayScore();

  let newScore = Number(document.forms["updateScoreForm"].elements[1].value) + 1;
  document.forms["updateScoreForm"].elements[1].value = newScore;
  document.getElementById("score").textContent = newScore;
}


//function warningMike(){
  //window.alert("¡¡ATENCIÓN!!\n\nEste juego es adictivo, te advertimos que en caso de querer jugar lo hagasbajo tu propia responsabilidad.\nHemos tenido casosde personas que se han olvidad de satisfacer sus
    //    necesidades vitales como; comer, hidratarse, poner un ladrillo,
      //  sexo, ... Bueno este último no, los jugadores de este juego
        //jamás han tenido sexo.\nEn definitiva, disfruta del juego,
        //compite contra tus amigos y no te olvides de que tienes otra
        //vida maldita sea!"
      //);
  //}


function updateScore(){
  let score = document.forms["updateScoreForm"].elements[1].value;
  document.forms["updateScoreForm"].action +=  score;
  document.forms["updateScoreForm"].submit();
}
