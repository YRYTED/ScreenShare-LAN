const img = document.getElementById("screen");


const socket = new WebSocket(
    "ws://" +
    location.host +
    "/stream"
);


socket.onmessage = function(event){

    img.src =
    "data:image/jpeg;base64," +
    event.data;

};