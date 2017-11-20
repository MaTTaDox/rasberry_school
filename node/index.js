var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var Redis = require('ioredis');
var redis = new Redis();
var pubSub = new Redis();



io.on('connection', function (socket) {
    console.log('a user connected');
    socket.on('disconnect', function () {
        io.emit('connected_user', connectedUser);
    });

});

pubSub.on('rfid_authentication', function (pattern, channel, message) {
    // Receive message Hello world! from channel news
    // Receive message Hello again! from channel music
    console.log('Receive message %s from channel %s and pattern %s', message, channel, pattern);
    io.emit(channel, message);
});

http.listen(3000, function () {
    console.log('listening on *:3000');
});
