const WebSocket = require('ws');

const wss = new WebSocket.Server({
		port: 3000
}, () => {
	console.log("Websocket ready");
	wss.on('connection', ws => {
		ws.send("Hello from the server");
		ws.on('message', data => {
			console.log(data.toString())
		});
	});
});
 
