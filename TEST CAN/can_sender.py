import can
import time

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

while True:
    message = can.Message(
        arbitration_id=0x123,  # CAN ID
        data=[0xDE, 0xAD, 0xBE, 0xEF],  
        is_extended_id=False  
    )
    bus.send(message)  
    print("Sent CAN Message")
    time.sleep(1)

