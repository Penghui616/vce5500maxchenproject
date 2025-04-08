from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('vehicle_data')
def handle_vehicle_data(data):
    print("Vehicle data received：", data)
    # 转发给所有连接的警车终端
    socketio.emit('forwarded_vehicle_data', data)

if __name__ == '__main__':
    socketio.run(app, port=5000)

