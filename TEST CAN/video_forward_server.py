import cv2
import socket
import struct
import pickle
from flask import Flask, Response

app = Flask(__name__)
frame_buffer = None

@app.route('/video_feed')
def video_feed():
    def generate():
        global frame_buffer
        while True:
            if frame_buffer is not None:
                ret, jpeg = cv2.imencode('.jpg', frame_buffer)
                if ret:
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

def receive_video():
    global frame_buffer
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(1)
    print("🟡 Waiting for connection...")
    conn, _ = server_socket.accept()
    print("🟢 Connected to stream.")

    data = b""
    payload_size = struct.calcsize(">L")

    while True:
        while len(data) < payload_size:
            packet = conn.recv(4096)
            if not packet:
                print("❌ No data. Closing.")
                return
            data += packet

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]

        while len(data) < msg_size:
            packet = conn.recv(4096)
            if not packet:
                print("❌ Connection lost.")
                return
            data += packet

        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame_buffer = pickle.loads(frame_data)
        print("🟢 Received frame.")

if __name__ == '__main__':
    import threading
    t = threading.Thread(target=receive_video)
    t.start()
    app.run(host='0.0.0.0', port=8081)

