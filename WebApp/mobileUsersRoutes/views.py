from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from mobileUsers.models import MobileUser
from routes.models import Route
from trackingRoutes.models import TrackingRoute
from mobileUsersRoutes.models import MobileUserRoute
from trackingPoints.models import TrackingPoint
from address.models import Address
import datetime

# Create your views here.

def setRoute(request, num):
	context = RequestContext(request)
	now = datetime.datetime.now()

	mobileUser = MobileUser.objects.get(pk=num)
	routes = Route.objects.all()
	if request.method == 'POST':
		date = request.POST.get("doDate", str(now))

	_id = request.POST.get("set", "")
	if _id:
		route = Route.objects.get(pk=int(_id.split('#')[1]))	
		mobileUserRoute = MobileUserRoute(route = route, mobileUser = mobileUser, trackingRoute = None, date = date)
		mobileUserRoute.save()
		return HttpResponseRedirect('mobileUsers')

	return render_to_response("setRoute.html",
				locals(),
				context_instance=RequestContext(request))


def trackMobileUser(request, num):
	mobileUser = MobileUser.objects.get(pk=num)

	now = datetime.datetime.now().strftime("%Y-%m-%d") 
	routeQuery = "select * from \"mobileUsersRoutes_mobileuserroute\" where date = '" + now + "';"
	routes = MobileUserRoute.objects.raw(routeQuery)

	if len(list(routes)) != 0 :
		routeId = routes[0].trackingRoute_id
		routeName =  TrackingRoute.objects.filter(pk = routeId).values('name')[0]
                print routeId

		lats = TrackingPoint.objects.filter(route=routeId).values('latitude')
		lons = TrackingPoint.objects.filter(route=routeId).values('longitude')

		latsList = []
		lonsList = []

		for lat in lats:
			latsList.extend(lat.values())

		for lon in lons:
			lonsList.extend(lon.values())


	return render_to_response("trackMobileUser.html",
								locals(),
								context_instance=RequestContext(request))


def mobileUserHistory(request, num):
	mobileUser = MobileUser.objects.get(pk=num)

	
	return render_to_response("mobileUserHistory.html",
								locals(),
								context_instance=RequestContext(request))
