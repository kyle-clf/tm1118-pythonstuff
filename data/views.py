from django.http import request
from django.shortcuts import render, redirect
from . import data_mqtt

from .models import Event
from django.http import JsonResponse
from django.core import serializers



from django.views.decorators.csrf import csrf_exempt


import datetime
import json
from django.db.models import Avg

# Create your views here.
def index(req):

    return render(req, 'data/index.html')


def dashboard(req):

    return render(req, 'data/dashboard.html')


def test(req):
    events = Event.objects.values("node_loc").distinct()
    ctx = {'testdata': events} 
    return render(req, 'data/test.html',ctx)

# def datatest(req):
#     events = Event.objects.all()
#     ctx = {'event': events}
#     return render(req, 'data/testdata.html', ctx)

def log(req):
    events = Event.objects.all().order_by("-date_created")[:100]
    listLocation = Event.objects.values("node_loc").distinct()
    ctx = {'events': events}
    ctx['listLocation'] = listLocation
    return render(req, 'data/log.html', ctx)


def showA07(req):
    ctx = {}
    ctx['node_id'] = "A07"
    events = Event.objects.filter(node_id=ctx['node_id']).order_by("-date_created")
    ctx['events'] =  events
    
    
    return render(req, 'data/datashow.html', ctx)

def data_events(req):
    events = Event.objects.all().order_by("-date_created")[:10]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)

def data_dashboard(req):
    events = Event.objects.all().order_by("-date_created")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)


def data_test2(req):
    d = datetime.datetime.now().replace(second=0, microsecond=0) -  datetime.timedelta(minutes = 2)
 
    events = Event.objects.filter(date_created__gte = d, date_created__lt = d +  datetime.timedelta(minutes = 1))
    print(events.aggregate(Avg('temp'))["temp__avg"])
    print(events.aggregate(Avg('hum'))["hum__avg"])
    print(events.aggregate(Avg('light'))["light__avg"])
    print(events.aggregate(Avg('snd'))["snd__avg"])
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)


@csrf_exempt
def data_test(req):
    ctx = {}
    if req.method == 'POST':
    
        postData = json.dumps(req.POST)
        try:
            events = Event.objects.filter(node_loc=req.POST["node_loc"]).order_by("-date_created")[:10]
    
            eventsData = serializers.serialize('json', events)
            return JsonResponse(eventsData, safe=False)

        except:
            return JsonResponse(postData, safe=False)
      
        postData = json.dumps(req.POST)
      
        return JsonResponse(postData, safe=False)
        # return redirect('/blog/')


    else:
    
        return render(req, 'data/datatest.html', ctx)

def data_dashboardA01(req):
    events = Event.objects.filter(node_id='A01').order_by("-date_created")[:7]
    
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)

