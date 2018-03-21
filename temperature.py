import paho.mqtt.client as mqtt

temp_file = open("/sys/bus/w1/devices/28-00000890bf46/w1_slave", "r")
temp_raw = temp_file.read()
temp_value = temp_raw[-6:-1]
temp_base = float(temp_value) / 1000
print temp_base

broker="192.168.1.212"

client = mqtt.Client("sensor1")
client.connect(broker)
client.publish("house/temp/1", temp_base)
client.disconnect()
