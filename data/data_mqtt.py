import paho.mqtt.client as mqtt
from .models import Event
from django.http import JsonResponse
from django.core import serializers
import json
import threading
from django.db.models.functions import Cast
from django.db.models import TextField

def on_connect(client, userdata, flags, rc):
    client.subscribe("iot/sensor")
    client.subscribe("iot/request")


def on_message(client, userdata, msg):
    iotData = (msg.payload.decode('utf-8'))
    try:
        iotData = json.loads(iotData)
        if "request" in iotData:
            events = Event.objects.filter(node_id=iotData["loc"]).values('node_id','node_loc','temp','hum','light','snd').order_by("-date_created")[:1]
            data = list(events)
            data = str(data)
            data = data.replace("\'", "\"")
            data = data.replace("[", " ")
            data = data.replace("]", " ")
            print(data)
            client.publish("iot/server", data)
        else:
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


# client = mqtt.Client()



# client.on_connect = on_connect
# client.on_message = on_message

# client.connect("ia.ic.polyu.edu.hk", 1883)
# client.loop_start()
