from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Bulding , Other, Path
import json

# Create your views here.
SUCCESS = "success"
FAIL = "fail"

def home(request):
    return HttpResponse(json.dumps("testing"), content_type="application/json")

def add_building(request):
    if request.method == "POST":
        building  = Bulding(buildingRequest = request.POST['buildingRequest'], wheelchair =request.POST['wheelchair'],
                            rating =request.POST['rating'],
                            improvement =request.POST['improvement'],
                            elevator = request.POST['elevator'],
                            toilets = request.POST['toilets'],
                            access =request.POST['access'],
                            longitude =request.POST['longitude'],
                            latitude =request.POST['latitude'])
        building.save()
        data = {"result":SUCCESS}
    else:
        data = {"result":FAIL,"error":"Invalid request","meta":"use POST method" }
    return HttpResponse(json.dumps(data), content_type="application/json")

def add_other(request):
    if request.method == "POST":
        other = Other(typeCrossing = request.POST['typeCrossing'],busStop = request.POST['busStop'],
                        barrier = request.POST['barrier'],
                        sidewalk = request.POST['sidewalk'],
                        rating = request.POST['rating'],
                        improvement = request.POST['improvement'],
                        longitude = request.POST['longitude'],
                        latitude = request.POST['latitude'])
        other.save()
        data = {"result":SUCCESS}
    else:
        data = {"result":FAIL,"error":"Invalid request","meta":"use POST method" }
    return HttpResponse(json.dumps(data), content_type="application/json")

def add_path(request):
    if request.method == "POST":
        path  = Path(smoothness = request.POST['smoothness'],surface = request.POST['surface'],
                        width = request.POST['width'],
                        slope = request.POST['slope'],
                        way = request.POST['way'],
                        wheelchair = request.POST['wheelchair'],
                        rating = request.POST['rating'],
                        improvement = request.POST['improvement'],
                        longitude = request.POST['longitude'],
                        latitude = request.POST['latitude'])

        path.save()
        data = {"result":SUCCESS}
    else:
        data = {"result":FAIL,"error":"Invalid request","meta":"use POST method" }
    return HttpResponse(json.dumps(data), content_type="application/json")

def get_path(request):
    data = []
    try:
        paths  = Path.objects.all()
        for path in paths:
            data.append({"smoothness":path.smoothness,"surface": path.surface,"width" :path.width,"slope" :path.slope,
                           "way" :path.way,"wheelchair" : path.wheelchair,"rating" :path.rating,
                           "improvement":  path.improvement,"longitude" : path.longitude,"latitude": path.latitude})
        response_data = {"result":SUCCESS,"data":data}
    except:
         response_data = {"result":FAIL,"error":"something went wrong with db","meta":"DB not accessable" }

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_other(request):
    data = []
    try:
        others  = Other.objects.all()
        for other in others:
            data.append({"typeCrossing":other.typeCrossing, "latitude":other.latitude, "improvement": other.improvement,
                         "barrier":other.barrier,"sidewalk":other.sidewalk,"busStop":other.busStop,"rating":other.rating,
                         "longitude":other.longitude,})
        response_data = {"result":SUCCESS,"data":data}
    except:
         response_data = {"result":FAIL,"error":"something went wrong with db","meta":"DB not accessable" }

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_building(request):
    data = []
    try:
        buildings  = Bulding.objects.all()
        for building in buildings:
            data.append({'buildingRequest':building.buildingRequest, 'wheelchair':building.wheelchair,'rating':building.rating,
                         'improvement':building.improvement,'elevator':building.elevator,'toilets':building.toilets,
                         'access':building.access,'longitude':building.longitude,'latitude':building.latitude})
        response_data = {"result":SUCCESS,"data":data}
    except:
         response_data = {"result":FAIL,"error":"something went wrong with db","meta":"DB not accessable" }
    return HttpResponse(json.dumps(response_data), content_type="application/json")