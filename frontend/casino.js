var game = {
    "players": [],
    "deck": [],
    "center": []
};

var cards = [
    "c_1", "c_2", "c_3", "c_4", "c_5", "c_6", "c_7", "c_8", "c_9", "c_10", "c_11", "c_12", "c_13",
    "d_1", "d_2", "d_3", "d_4", "d_5", "d_6", "d_7", "d_8", "d_9", "d_10", "d_11", "d_12", "d_13",
    "h_1", "h_2", "h_3", "h_4", "h_5", "h_6", "h_7", "h_8", "h_9", "h_10", "h_11", "h_12", "h_13",
    "s_1", "s_2", "s_3", "s_4", "s_5", "s_6", "s_7", "s_8", "s_9", "s_10", "s_11", "s_13", "s_12"
]

class Card {
    constructor(name) {
        this.name = name;
        this.value = name.split("_")[1];
        this.builtValue = this.value;
        this.wasLastPlayed = false;
    }
}

function setup(playerNames){


    for (playerName of playerNames) {
        var player = {
            "name": playerName
        }
        
    }
};

cardtest = new Card("c_12");

var test = ["asdf", "fdsa"];
setup(test);





console.log(game)