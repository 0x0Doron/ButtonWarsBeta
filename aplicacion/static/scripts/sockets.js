const socket = io();

socket.emit('message', 'Conexión iniciada');  // message es el evento por el que enviamos y recibimos
socket.on('message', function (msg){
  $('#messages').append('<li style="color: white;">' + msg + '</li>');
});

$('#send').on('click', function(){
  socket.send($('#myMessage').val());
  $('#myMessage').val('');  //Borramos el input
});
