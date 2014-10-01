from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from trackingRoutes.models import TrackingRoute
from address.models import Address
from points.models import Point

def trackAll(request):
        routesCount = TrackingRoute.objects.count()
        routes = TrackingRoute.objects.all()
        print "HERE"
        print routesCount
        routesAddresses = []
        routesLat = []
        routesLon = []

        for route in routes:
            lats = Point.objects.filter(route=route.id).values('latitude')
            lons = Point.objects.filter(route=route.id).values('longitude')

            latsList = []
            lonsList = []
            addsList = []

	    for add in adds:
		addsList.append(str(add.street)+' '+ str(add.number)+', '+str(add.postCode)+' '+ str(add.city))

            for lat in lats:
                    latsList.extend(lat.values())

            for lon in lons:
                    lonsList.extend(lon.values())
            
            routesAddresses.append(addsList)
            routesLat.append(latsList)
            routesLon.append(lonsList)


	context = RequestContext(request)
	return render_to_response("trackAll.html",
								locals(),
								context_instance=RequestContext(request))
