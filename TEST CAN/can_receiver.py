import can

# 连接到虚拟 CAN 总线 vcan0
bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

print("Listening for CAN messages...")
while True:
    message = bus.recv()  # 接收 CAN 消息
    print(f"Received CAN Message: ID={hex(message.arbitration_id)}, Data={message.data}")

