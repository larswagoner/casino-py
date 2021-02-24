var game = {
    "players": [],
    "deck": [],
    "center": []
};

class Card {
    constructor(name) {
        this.name = name;
        this.value = name.split("_")[1];
        this.builtValue = this.value;
        this.wasLastPlayed = false;
    }
}

function createDeck(){
    for (letter of ["c", "d", "h", "s"]) {
        for(i = 1; i < 14; i++){
            game.deck.push(new Card(i + "_" + letter));
        }
    }
}
createDeck();






console.log(game)