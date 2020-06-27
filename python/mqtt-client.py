import paho.mqtt.client as mqtt

ADDRESSS = "mqtt.eclipse.org"
PORT = 1883

client = mqtt.Client()

topics = [
    ('bed_room_led', 1),
    ('water_moter_outside', 2),
]


def on_connect(_client, _userdata, _flags, _rc):
    print(f"connect result : {_userdata} \t {_flags} \t {_rc}")


def on_message(_client, _userdata, _message):
    print(f"message:  {_userdata} \t {_message.payload}")


client.on_connect = on_connect
client.on_message = on_message

client.connect(ADDRESSS, PORT)
client.subscribe(topics)

client.loop_forever()
