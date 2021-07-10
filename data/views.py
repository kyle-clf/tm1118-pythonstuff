from django.http import request
from django.shortcuts import render, redirect
from . import data_mqtt
from . import getVenueEvent


from .models import Event
from .models import VenueEvent
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
    return render(req, 'data/test.html', ctx)

# def datatest(req):
#     events = Event.objects.all()
#     ctx = {'event': events}
#     return render(req, 'data/testdata.html', ctx)


def log(req):
    events = Event.objects.all().order_by("-date_created")[:20]
    listLocation = Event.objects.values("node_loc").distinct()
    ctx = {'events': events}
    ctx['listLocation'] = listLocation
    return render(req, 'data/log.html', ctx)

def logd(req):
    events = Event.objects.all().order_by("-date_created")[:1000]
    listLocation = Event.objects.values("node_loc").distinct()
    ctx = {'events': events}
    ctx['listLocation'] = listLocation
    return render(req, 'data/logtable.html', ctx)


def queryForm(req):

    ctx = {}
    ctx['postData'] = json.dumps(req.POST)
    print(ctx['postData'])
    return render(req, 'data/queryForm.html', ctx)

@csrf_exempt
def queryResult(req):

    ctx = {}
    ctx['start'] = req.POST['start']
    ctx['end'] = req.POST['end']
    ctx['location'] = req.POST['location']
    dStart = datetime.datetime.strptime(ctx['start'], '%Y-%m-%dT%H:%M')
    dEnd = datetime.datetime.strptime(ctx['end'], '%Y-%m-%dT%H:%M')
 
    ctx['events'] = Event.objects.filter(date_created__gte=dStart, date_created__lt=dEnd,node_loc=ctx['location']).order_by("-date_created")
    ctx['events'] = serializers.serialize('json', ctx['events'])
    
    return JsonResponse(json.dumps(ctx), safe=False)



def showA07(req):
    ctx = {}
    ctx['node_id'] = "A07"
    events = Event.objects.filter(
        node_id=ctx['node_id']).order_by("-date_created")
    ctx['events'] = events

    return render(req, 'data/datashow.html', ctx)


def data_events(req):
    events = Event.objects.all().order_by("-date_created")[:10]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)


def data_dashboard(req):
    events = Event.objects.all().order_by("-date_created")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)


def graph_overview(req):
    ctx = {}
    return render(req, 'data/showGraphByCat.html', ctx)

def location(req):
    ctx = {}
    return render(req, 'data/showGraphByCat.html', ctx)



def data_test2(req):
    d = datetime.datetime.now().replace(second=0, microsecond=0) - \
        datetime.timedelta(minutes=2)

    events = Event.objects.filter(
        date_created__gte=d, date_created__lt=d + datetime.timedelta(minutes=1))
    print(events.aggregate(Avg('temp'))["temp__avg"])
    print(events.aggregate(Avg('hum'))["hum__avg"])
    print(events.aggregate(Avg('light'))["light__avg"])
    print(events.aggregate(Avg('snd'))["snd__avg"])
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)


@csrf_exempt
def data_test1(req):
    ctx = {}
    if req.method == 'POST':

        postData = json.dumps(req.POST)
        try:
            events = Event.objects.filter(
                req.POS.node_loc).order_by("-date_created")[:10]

            eventsData = serializers.serialize('json', events)
            print(eventsData)
            if eventsData == []:
                print('err')
                raise Exception
            return JsonResponse(eventsData, safe=False)
            


        except:
            locList = ['W311-H1', 'W311-H2', 'W311-H3', 'W311A', 'W311B', 'W311D-Z1', 'W311D-Z2']
            events = {}
            for x in locList:
                events[x] = Event.objects.filter(x).order_by("-date_created")[:10]
                events[x]  = serializers.serialize('json', x)
           

            eventsData = json.dumps(events)
            print(eventsData)
            return JsonResponse(eventsData, safe=False)

        postData = json.dumps(req.POST)

        return JsonResponse(postData, safe=False)
        # return redirect('/blog/')

    else:

        return render(req, 'data/datatest.html', ctx)


@csrf_exempt
def data_test(req):
    ctx = {}
    if req.method == 'POST':

        postData = json.dumps(req.POST)
        try:
            events = Event.objects.filter(
                node_loc=req.POST["node_loc"]).order_by("-date_created")[:10]

            eventsData = serializers.serialize('json', events)
            print(eventsData)
            if str(eventsData) == "[]":
                raise Exception
            return JsonResponse(eventsData, safe=False)
            

        except:
            locList = ['W311-H1', 'W311-H2', 'W311-H3', 'W311A', 'W311B', 'W311D-Z1', 'W311D-Z2']
            events = []
            for x in locList:
                
                event = Event.objects.filter(node_loc=x).order_by("-date_created")[:10]
                events.append(serializers.serialize('json', event))
           
           

            eventsData = json.dumps(events)

            return JsonResponse(eventsData, safe=False)

        postData = json.dumps(req.POST)

        return JsonResponse(postData, safe=False)
        # return redirect('/blog/')

    else:

        return render(req, 'data/datatest.html', ctx)


def data_dashboardA01(req):
    events = Event.objects.filter(node_id='A01').order_by("-date_created")[:7]
    eventsData = serializers.serialize('json', events)
    return JsonResponse(eventsData, safe=False)


@csrf_exempt
def excel(req):
    VenueEvents = VenueEvent.objects.all()
    ctx = {'VenueEvents': VenueEvents}
    if req.method == 'POST':
        postData = json.dumps(req.POST)
        try:
            startdate = req.POST["startdate"]
            starttime = req.POST["starttime"]
            enddate = req.POST["enddate"]
            endtime = req.POST["endtime"]
            print(startdate)
            print(enddate)
            VenueEvents = VenueEvent.objects.filter(date__gte=startdate, date__lte=enddate).order_by("-date")
            ctx = {'VenueEvents': VenueEvents}
            return render(req, 'data/excel.html', ctx)
        except Exception as e:
            print(e)
            return render(req, 'data/excel.html', ctx)
        # return redirect('/blog/')

    else:
        VenueEvents = VenueEvent.objects.all()
        ctx = {'VenueEvents': VenueEvents}
        return render(req, 'data/excel.html', ctx)