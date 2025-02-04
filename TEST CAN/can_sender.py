import can
import time

# 连接到虚拟 CAN 总线 vcan0
bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

while True:
    message = can.Message(
        arbitration_id=0x123,  # CAN ID
        data=[0xDE, 0xAD, 0xBE, 0xEF],  # 数据
        is_extended_id=False  # 标准帧
    )
    bus.send(message)  # 发送消息
    print("Sent CAN Message")
    time.sleep(1)

