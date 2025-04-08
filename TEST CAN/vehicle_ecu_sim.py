import time
import random
import socketio

# 初始化SocketIO客户端
sio = socketio.Client()
sio.connect('http://localhost:5000')  # 假设Edge服务器地址是 localhost:5000

# 模拟 VIN 和档位
VIN = "1HGCM82633A004352"
PRNDL = "D"  # D档

# 生成最近5分钟，每10秒一次的速度数据（总共30条）
speed_data = [random.randint(0, 100) for _ in range(30)]

def send_vehicle_data():
    for i in range(30):
        data = {
            "vin": VIN,
            "prndl": PRNDL,
            "speed": speed_data[i],
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        sio.emit('vehicle_data', data)
        print("send data：", data)
        time.sleep(1)  # 模拟每10秒采样，测试用缩短成1秒

send_vehicle_data()

