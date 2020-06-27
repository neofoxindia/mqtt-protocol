import paho.mqtt.client as mqtt
import time
from concurrent.futures import ThreadPoolExecutor


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

def print_time():
    while True:
        time.sleep(1)
        print(time.time())



with ThreadPoolExecutor(max_workers = 2) as executer:
    mqtt_loop = executer.submit(client.loop_forever)
    time_func = executer.submit(print_time)
