import can
import time

# Connect to the CAN bus
bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

# PRNDL state mapping
PRNDL_VALUES = [0x00, 0x01, 0x02, 0x03, 0x04]  # P, R, N, D, L
PRNDL_NAMES = {0x00: "P", 0x01: "R", 0x02: "N", 0x03: "D", 0x04: "L"}

index = 0

while True:
    prndl_status = PRNDL_VALUES[index]
    message = can.Message(arbitration_id=0x123, data=[prndl_status], is_extended_id=False)
    bus.send(message)
    print(f"Sent PRNDL CAN Message: {PRNDL_NAMES[prndl_status]}")
    
    index = (index + 1) % len(PRNDL_VALUES)  # Cycle through P-R-N-D-L
    time.sleep(2)  # Switch state every 2 seconds

