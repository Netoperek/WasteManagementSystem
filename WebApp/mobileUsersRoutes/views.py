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


def mobileUsersRoutes(request, num):
	_id = request.POST.get("unset", "")
	if _id:
		MobileUserRoute.objects.filter(route_id=int(_id.split('#')[1])).delete()

	query = 'select routes_route.id, routes_route.name, date from routes_route inner join "mobileUsersRoutes_mobileuserroute" on (routes_route.id = "mobileUsersRoutes_mobileuserroute".route_id) where "mobileUsersRoutes_mobileuserroute"."mobileUser_id" =' +str(num)+' ;'

	routes = Route.objects.raw(query)
	return render_to_response("mobileUsersRoutes.html",
								locals(),
								context_instance=RequestContext(request))
def setRoute(request, num):
	context = RequestContext(request)
        routeId = -1 

        notSet = True
        _id = request.POST.get("set", "")
        if _id:
            routeId = int(_id.split('#')[1])
        
        if MobileUserRoute.objects.filter(route_id = routeId):
                notSet = False
        else:
                mobileUser = MobileUser.objects.get(pk=num)
                routes = Route.objects.all()

                if _id:
			date = request.POST['date']
                        if date:
                            route = Route.objects.get(pk=routeId)	
                            mobileUserRoute = MobileUserRoute(route = route, mobileUser = mobileUser, date = date)
                            mobileUserRoute.save()
                            return HttpResponseRedirect('mobileUsersRoutes' + str(num))

	return render_to_response("setRoute.html",
				locals(),
				context_instance=RequestContext(request))

def setUserToRoute(request, num):

        notSet = True
        if MobileUserRoute.objects.filter(route_id = num):
                notSet = False
        else:
                mobileUsers = MobileUser.objects.all()
                routeToSet = Route.objects.filter(id=num).values('name')[0]
                now = datetime.datetime.now()
                routeId = num
                _id = request.POST.get("set", "")
                if _id:
			date = request.POST['date']
                        if date:
                            route = Route.objects.get(pk=num)
                            mobileUser = MobileUser.objects.get(pk=int(_id.split('#')[1]))	
                            mobileUserRoute = MobileUserRoute(route = route, mobileUser = mobileUser, date = date)
                            mobileUserRoute.save()
                            return HttpResponseRedirect('mobileUsersRoutes' + str(mobileUser.id))
                
                else:
                        if request.method == 'POST':
                            Id = request.POST['id']
                            Login = request.POST['Login']

                            if Login == None:
                                Login = r".*"

                            if Id:
                                mobileUsers =  MobileUser.objects.filter(pk = Id, login__regex=Login)
                            else:
                                mobileUsers =  MobileUser.objects.filter(login__regex=Login)

        routeId = num
	return render_to_response("setUserToRoute.html",
								locals(),
								context_instance=RequestContext(request))


def trackMobileUser(request, num):
	mobileUser = MobileUser.objects.get(pk=num)

	now = datetime.datetime.now().strftime("%Y-%m-%d") 
	routeQuery = "select * from \"mobileUsersRoutes_mobileuserroute\" where date = '" + now + "';"
	routes = MobileUserRoute.objects.raw(routeQuery)

	if len(list(routes)) != 0 :
		routeId = routes[0].trackingRoute_id
                
                if routeId:
                    routeName =  TrackingRoute.objects.filter(pk = routeId).values('name')[0]

                    lats = TrackingPoint.objects.filter(route=routeId).values('latitude')
                    lons = TrackingPoint.objects.filter(route=routeId).values('longitude')

                    latsList = []
                    lonsList = []

                    for lat in lats:
                            latsList.extend(lat.values())

                    for lon in lons:
                            lonsList.extend(lon.values())


	return render_to_response(  "trackMobileUser.html",
				    locals(),
				    context_instance=RequestContext(request))


def mobileUserHistory(request, num):
	mobileUser = MobileUser.objects.get(pk=num)

	
	return render_to_response("mobileUserHistory.html",
								locals(),
								context_instance=RequestContext(request))
