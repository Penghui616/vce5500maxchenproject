import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_TOPIC = "v2v/prndl_status"

def on_message(client, userdata, msg):
    print(f"Received PRNDL Status from MQTT: {msg.payload.decode()}")

mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_BROKER, 1883)
mqtt_client.subscribe(MQTT_TOPIC)

print("Listening for PRNDL MQTT Messages...")
mqtt_client.loop_forever()  

