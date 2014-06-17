from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from points.models import Point
from routes.models import Route
from address.models import Address
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

def getStreet(address):
	return address.split(' ')[1][:-1]

def getNumber(address):
	return address.split(' ')[2][:-1]

def getCode(address):
	return address.split(' ')[3][:-1]

def getCity(address):
	return address.split(' ')[4][:-1]

def saveRoute(request):
	points = []
	if request.POST.has_key('points'):
		points = request.POST.getlist('points')
		routeName =  request.POST.get('routeName')
		route = Route(name = routeName)
		route.save()

		for point in points:
			address = getAddress(point)
		 	saveAddress = Address(street = getStreet(address), number = getNumber(address), postCode = getCode(address), city = getCity(address))
		 	saveAddress.save()
		 	savePoint = Point(route = route, address = saveAddress, longitude = getLongitude(point), latitude = getLatitude(point))
		 	savePoint.save()
		return HttpResponse('Trasa zapisana')

	return HttpResponse('Wybierz conajmniej jeden punkt')
