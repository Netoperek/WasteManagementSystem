from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest

from routes.models import Route
from points.models import Point
from mobileUsers.models import MobileUser
from address.models import Address
# Create your views here.

def routes(request):
	context = RequestContext(request)
	routes = Route.objects.all()

	_id = request.POST.get("remove", "")
	if _id:
		Route.objects.filter(id=int(_id.split('#')[1])).delete()

	else:
		if request.method == 'POST':
			Id = request.POST['Id']
			Name = request.POST['Name']

			if Name == None:
				Name = r".*"

			if Id:
				routes =  Route.objects.filter(pk = Id,
												name__regex=Name)
			else:
				routes =  Route.objects.filter(name__regex=Name)

	return render_to_response("routes.html",
								locals(),
								context_instance=RequestContext(request))

def routeDetails(request, num):
	routeId= num
	points = Point.objects.filter(route=num)
	return render_to_response("routeDetails.html",
								locals(),
								context_instance=RequestContext(request))

def routeOnMap(request, num):
	routeId= num
	addressQuery = 'select * from address_address join points_point on (address_address.id = points_point.address_id) where points_point.route_id =' + str(routeId) +' ;'
	lats = Point.objects.filter(route=num).values('latitude')
	lons = Point.objects.filter(route=num).values('longitude')
	adds = Address.objects.raw(addressQuery)

	latsList = []
	lonsList = []
	addsList = []
	
	for lat in lats:
		latsList.extend(lat.values())

	for lon in lons:
		lonsList.extend(lon.values())

	for add in adds:
		addsList.append(str(add.street)+' '+ str(add.number)+', '+str(add.postCode)+' '+ str(add.city))

	return render_to_response("routeOnMap.html",
								locals(),
								context_instance=RequestContext(request))


