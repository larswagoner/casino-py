const http = require('http');
const express = require('express');
const WebSocket = require('ws');


const port = 3100;

const server = http.createServer(express);

const wsServer = new WebSocket.Server({ server });

wsServer.on('connection', (ws) => {
    ws.on('message', (data) => {
        wsServer.clients.forEach((client) => {
            if(client !== ws && client.readyState === WebSocket.OPEN) {
                client.send(data);
            }
        })
    });
});

server.listen(port, () => {
    console.log("Server is listening on " + port);
})
