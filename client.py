import paho.mqtt.client as mqtt
import os, urlparse, select, sys

def on_connect(client, userdata, flags, rc):
	client.connected_flag = True
	print "ad client: " + str(client)	

def on_message(client, obj, msg):
	print "recieved msg is: " + msg.payload

def on_publish(client, obj, mid):
	print "published mid: " + str(mid)

def on_subscribe(client, obj, mid, granted_qos):
	print "msg id: "+ str(mid)
#def on_log(client, obj, level, string):

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

payload = ""
mqttc.connect("localhost", port=1883 ,keepalive=30, bind_address="127.0.0.1")
mqttc.subscribe("swiggy/tech", 0)
#mqttc.publish("swiggy/tech", payload)
# Continue the network loop, exit when an error occurs       

rc = 0
while rc == 0:
    mqttc.loop()
    if mqttc.connected_flag == True:
    	print "type YES in 5 seconds if you want to publish: "
    	timeout = 5
    	read, _, _ = select.select([sys.stdin], [], [], timeout)
    	if read:
    		yes = int(sys.stdin.readline())
    		if yes == 1:
    			payload = raw_input("input message to publish: ")
    			mqttc.publish("swiggy/tech", payload)
    		
