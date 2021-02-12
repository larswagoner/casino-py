const http = require('http');
const wsServer = require("ws").server
const httpServer = http.createServer();




httpServer.listen(3100, () => console.log("listening on 3100"));

//hasmap
const clients = {};

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
        //Received a message from client


    });

    const clientId = uuid();
    clients[client] = {
        "connection": connection
    };

});
 



