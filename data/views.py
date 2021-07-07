from django.http import request
from django.shortcuts import render, redirect
from . import data_mqtt

from .models import Event
from django.http import JsonResponse
from django.core import serializers








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
    events = Event.objects.all().order_by("-date_created")
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



def data_dashboardA01(req):
    events = Event.objects.filter(node_id='A01').order_by("-date_created")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)

def data_dashboardA02(req):
    events = Event.objects.filter(node_id='A02').order_by("-date_created")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)

def data_dashboardA03(req):
    events = Event.objects.filter(node_id='A03').order_by("-date_created")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)

def data_dashboardA04(req):
    events = Event.objects.filter(node_id='A04').order_by("-date_created")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)

def data_dashboardA05(req):
    events = Event.objects.filter(node_id='A05').order_by("-date_created")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)


def data_dashboardA06(req):
    events = Event.objects.filter(node_id='A06').order_by("-date_created")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)


def data_dashboardA07(req):
    events = Event.objects.filter(node_id='A07').order_by("-date_created")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)