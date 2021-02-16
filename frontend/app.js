var canvas = document.getElementById("mainTable");

var ctx = canvas.getContext("2d");
const height = window.innerHeight;
const width = window.innerWidth;
var cardWidth = width * 0.1;
var cardHeight = cardWidth*1.3;



let query = window.matchMedia("(max-width: 400px)");

if(query.matches){
    //wider than 400
    cardWidth = width * 0.2;
    cardHeight = cardWidth * 1.3;
} else {
    //narrower than 400px
    cardWidth = width * 0.1;
    cardHeight = cardWidth * 1.4;
}








canvas.width = width;
canvas.height = height;

ctx.fillStyle = "#33cc33";
ctx.fillRect(0, 0, width, height);

var image = new Image();
image.src = "https://www.cardgamesolitaire.com/game/images/gui/Spades_J.png";
image.onload = function(){
    ctx.drawImage(this, 0, 0, cardWidth, cardHeight);
}
var image2 = new Image();
image2.src = "https://www.cardgamesolitaire.com/game/images/gui/Spades_Q.png";
image2.onload = function(){
    ctx.drawImage(this, cardWidth, 0, cardWidth, cardHeight);
}
var image3 = new Image();
image3.src = "https://www.cardgamesolitaire.com/game/images/gui/Spades_K.png";
image3.onload = function(){
    ctx.drawImage(this, cardWidth*2, 0, cardWidth, cardHeight);
}
var image4 = new Image();
image4.src = "https://www.cardgamesolitaire.com/game/images/gui/Spades_A.png";
image4.onload = function(){
    ctx.drawImage(this, cardWidth*3, 0, cardWidth, cardHeight);
}

