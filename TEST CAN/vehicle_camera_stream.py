import cv2
import socket
import struct
import pickle
import time

# Connect to edge server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

video_path = "/home/abc/桌面/TEST CAN/car_view.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Cannot open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("✅ Video ended. Restarting...")
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    data = pickle.dumps(frame)
    size = struct.pack(">L", len(data))
    client_socket.sendall(size + data)
    print("🟢 Sent one frame.")
    time.sleep(1 / 25)  # Match video FPS



