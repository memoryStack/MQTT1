import paho.mqtt.publish as publish

while True:
	payload = raw_input("input payload: ")
	publish.single("swiggy/tech", payload=payload, hostname="localhost")