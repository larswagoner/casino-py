const http = require('http');

const wsServer = require("websocket").server
const httpServer = http.createServer();


// ---------- Host Webpage ----------
const app = require("express")();
app.get("/", (req, res) => res.sendFile(__dirname + "/index.html"));
app.listen(3000, () => console.log("listening on 3000"))
// ----------------------------------



httpServer.listen(3100, () => console.log("listening on 3100"));

//hasmap
const clients = {};
const games = {};

const ws = new wsServer({
    "httpServer": httpServer
}) 

// ---------- Helper Functions ----------
function uuid() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

ws.on("request", request => {
    //connection by client
    const connection = request.accept(null, request.origin);
    
    connection.on("open", () => console.log("opened"));
    connection.on("close", () => console.log("closed"));
    connection.on("message", message => {
        const result = JSON.parse(message.utf8Data);
        //Received a message from client
        if (result.method === "create"){
            const connectedClient = result.clientId;
            const gameId = uuid();
            games[gameId] = {
                "id": gameId,
                "balls": 20
            }
            const payLoad = {
                "method": "create",
                "game": games[gameId]
            }
            const con = clients[connectedClient].connection;
            con.send(JSON.stringify(payLoad));
        }

        if (result.method === "join") {
            const clientId = response.clientId;
            const gameId = response.gameId;
            const game = game

        }

    });

    const clientId = uuid();
    clients[clientId] = {
        "connection": connection
    };

    const payLoad = {
        "method": "connect",
        "clientId": clientId
    }

    //send back the client connect
    connection.send(JSON.stringify(payLoad))




});
 



