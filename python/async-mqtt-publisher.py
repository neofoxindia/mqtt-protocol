import paho.mqtt.client as mqtt
import time
from concurrent.futures import ThreadPoolExecutor


ADDRESSS = "mqtt.eclipse.org"
PORT = 1883

client = mqtt.Client()


def on_connect(_client, _userdata, _flags, _rc):
    print(f"connect result : {_userdata} \t {_flags} \t {_rc}")


def on_publish(_client, _userdata, _mid):
    print(f"Publish:  {_userdata} \t {_mid}")


client.on_connect = on_connect
client.on_publish = on_publish

client.connect(ADDRESSS, PORT)


def publisher():
    client.loop_start()

    for i in range(10):
        time.sleep(1)
        client.publish("led_light_home", "on", 1)
        time.sleep(1)
        client.publish("led_light_home", "off", 1)

    client.loop_stop()


def print_time():
    while True:
        time.sleep(1)
        print(time.time())


with ThreadPoolExecutor(max_workers=2) as executer:
    mqtt_loop = executer.submit(publisher)
    time_func = executer.submit(print_time)
