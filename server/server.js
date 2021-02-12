const http = require('http');
const wsServer = require("websocket").server
const httpServer = http.createServer();




httpServer.listen(3100, () => console.log("listening on 3100"));


const ws = new wsServer({
    "httpServer": httpServer
}) 

ws.on("request", request => {
    //connection by client
    const connection = request.accept(null, request.origin);
    connection.on("open", () => console.log("opened"));
    connection.on("close", () => console.log("closed"));
    connection.on("message", message => {
        //Received a message from client


    });





})
 
function S4() {
    return (((1+Math.random())*0x10000))
}


