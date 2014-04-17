from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from routes.models import Point
from routes.models import Route
# Create your views here.

def newRoute(request):
	return render_to_response("newRoute.html",
								locals(),
								context_instance=RequestContext(request))

def getLatitude(point):
	return float(point.split('#')[0])

def getLongitude(point):
	return float(point.split('#')[1])

def getAddress(point):
	return point.split('#')[2]

def saveRoute(request):
	points = request.GET.getlist('points')
	route = Route()
	route.save()
	for point in points:
		savePoint = Point(Route = route, Latitude = getLatitude(point), Longitude = getLongitude(point),Address = getAddress(point))
		savePoint.save()
	return HttpResponse('Route is Saved')
