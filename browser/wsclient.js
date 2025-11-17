const ws = new WebSocket('ws://ws.midnight-worker.de:3333');

ws.onmessage = data => {
    console.log(data);
    ws.send("hallo welt");
}