//  **`frontend/app.js`** - JavaScript for handling moves and WebSocket communication

const board = Chessboard('chessboard', {
    draggable: true,
    position: 'start',
    onDrop: onDrop
});


window.Telegram.WebApp.ready();

function onDrop(source, target) {
    const move = game.move({ from: source, to: target });
    if (move === null) return 'snapback';

        sendMoveToBackend(source, target);
}

function sendMoveToBackend(source, target) {
    const token = Telegram.WebApp.initData;
    fetch('https://bot-bee.online/api/move', { 
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ source, target })
    });
}

const socket = new WebSocket('wss://bot-bee.online/ws/game');
socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    board.move(data.source, data.target);
};
