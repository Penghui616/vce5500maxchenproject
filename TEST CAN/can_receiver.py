import can

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

print("Listening for CAN messages...")
while True:
    message = bus.recv() 
    print(f"Received CAN Message: ID={hex(message.arbitration_id)}, Data={message.data}")

