import paho.mqtt.client as mqtt


from .models import Event
import json




def on_connect(client, userdata, flags, rc):
    client.subscribe("iot/sensor")


def on_message(client, userdata, msg):
    iotData = (msg.payload.decode('utf-8'))
    
    try:
        iotData = json.loads(iotData)
        p = Event(node_id=iotData["node_id"],
                  node_loc=iotData["loc"],
                  temp=int(float(iotData["temp"])),
                  hum=int(float(iotData["hum"])),
                  light=int(float(iotData["light"])),
                  snd=int(float(iotData["snd"])),
                  )
        p.save()
        print("success: " + str(iotData))

    except Exception as k:
        print(k.args)
        print("error: " + str(iotData))
        pass


client = mqtt.Client()



client.on_connect = on_connect
client.on_message = on_message

client.connect("ia.ic.polyu.edu.hk", 1883)
client.loop_start()
