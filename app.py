from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clavesecretaXD'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def inicio():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    room = data.get('room')
    join_room(room)
    print(f"Un usuario se unió al {room}")

@socketio.on('leave')
def handle_leave(data):
    room = data.get('room')
    leave_room(room)
    print(f"Un usuario salió del {room}")
@socketio.on('audio_stream')
def handle_audio_stream(data):
    room = data.get('room')
    username = data.get('username', 'Anónimo')
    audio_data = data.get('audio')
    mime_type = data.get('mime', 'audio/webm')  
    
    emit('audio_stream', {
        'username': username,
        'audio': audio_data,
        'mime': mime_type                      
    }, to=room, include_self=False)
if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
