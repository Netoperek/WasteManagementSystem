from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from trackingRoutes.models import TrackingRoute
from address.models import Address
from mobileUsers.models import MobileUser
from mobileUsersRoutes.models import MobileUserRoute
from trackingPoints.models import TrackingPoint

def trackAll(request):
        routesCount = TrackingRoute.objects.count()
        trackingRoutes = TrackingRoute.objects.all()
        routesLat = []
        routesLon = []

        for trackingRoute in trackingRoutes:
            lats = TrackingPoint.objects.filter(trackingRoute=trackingRoute.id).values('latitude')
            lons = TrackingPoint.objects.filter(trackingRoute=trackingRoute.id).values('longitude')

            latsList = []
            lonsList = []
            addsList = []

            for lat in lats:
                    latsList.extend(lat.values())

            for lon in lons:
                    lonsList.extend(lon.values())
            
            routesLat.append(latsList)
            routesLon.append(lonsList)

	context = RequestContext(request)
	return render_to_response("trackAll.html",
								locals(),
								context_instance=RequestContext(request))

def trackingRouteDetails(request, num):
    points = TrackingPoint.objects.filter(trackingRoute=num)
    return render_to_response("trackingRouteDetails.html",
                                locals(),
                                context_instance=RequestContext(request))
