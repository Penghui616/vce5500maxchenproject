import can
import time
import paho.mqtt.client as mqtt

# Connect to the MQTT broker
MQTT_BROKER = "localhost"
MQTT_TOPIC = "v2v/prndl_status"

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, 1883)

# Connect to the CAN bus
bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

# PRNDL status mapping
PRNDL_MAP = {
    0x00: "P (Park)",
    0x01: "R (Reverse)",
    0x02: "N (Neutral)",
    0x03: "D (Drive)",
    0x04: "L (Low)"
}

print("Listening for PRNDL CAN Messages...")

while True:
    message = bus.recv()  # Read CAN data
    if message.arbitration_id == 0x123:  # Listen for PRNDL status
        prndl_status = message.data[0]
        status_text = PRNDL_MAP.get(prndl_status, "Unknown")
        
        print(f"Received PRNDL Status: {status_text}")

        # Send to MQTT
        mqtt_client.publish(MQTT_TOPIC, status_text)
        print(f"Sent to MQTT: {status_text}")

