from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from mobileUsers.models import MobileUser
from routes.models import Route
from trackingRoutes.models import TrackingRoute
from mobileUsersRoutes.models import MobileUserRoute
from trackingPoints.models import TrackingPoint
from address.models import Address
import datetime

def mobileUsersRoutes(request, num):
	_id = request.POST.get("_id")
	query = 'select routes_route.id, routes_route.name, date from routes_route inner join "mobileUsersRoutes_mobileuserroute" on (routes_route.id = "mobileUsersRoutes_mobileuserroute".route_id) where "mobileUsersRoutes_mobileuserroute"."mobileUser_id" =' +str(num)+' ;'
	routes = Route.objects.raw(query)
        userId = num
        routesResult = []
        routesId = []
        routesDate = []
        queryDate = []

	if _id:
		MobileUserRoute.objects.filter(route_id=_id).delete()
	else:
		if request.method == 'POST':
			Id = request.POST['Id']
			Name = request.POST['Name']
			Date = request.POST['Date']
                        routesSet = request.POST.get("set","")

			if Id:
                            queryId = 'select routes_route.id, routes_route.name, date from routes_route inner join "mobileUsersRoutes_mobileuserroute" on (routes_route.id = "mobileUsersRoutes_mobileuserroute".route_id) where "mobileUsersRoutes_mobileuserroute"."mobileUser_id" =' +str(num)+' and routes_route.id = ' +str(Id) + ';'
                            routes = Route.objects.raw(queryId)
                        else:
                            queryId = query

                        if Date:
                            if not validate(Date):
                                return HttpResponseRedirect('passDate' + str(num))
                            queryDate = 'select routes_route.id, routes_route.name, date from routes_route inner join "mobileUsersRoutes_mobileuserroute" on (routes_route.id = "mobileUsersRoutes_mobileuserroute".route_id) where "mobileUsersRoutes_mobileuserroute"."mobileUser_id" =' +str(num)+' and date = \'' +str(Date) + '\' intersect ' + str(queryId) + ' ;'
                            routes = Route.objects.raw(queryDate)
                        else:
                            queryDate = query

                        if Name:
                            queryName = 'select routes_route.id, routes_route.name, date from routes_route inner join "mobileUsersRoutes_mobileuserroute" on (routes_route.id = "mobileUsersRoutes_mobileuserroute".route_id) where "mobileUsersRoutes_mobileuserroute"."mobileUser_id" =' +str(num)+' and name = \'' +str(Name) + '\' intersect ' + str(queryDate) + ' ;'
                            routes = Route.objects.raw(queryName)

	return render_to_response("mobileUsersRoutes.html",
								locals(),
								context_instance=RequestContext(request))


def passDate(request, num):
    num
    return render_to_response("passDate.html",
                            locals(),
                            context_instance=RequestContext(request))

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def getNotSetRoutes(routes):
        routesNotSet = []

        for route in routes:
            mobileUserRoutes = MobileUserRoute.objects.filter(route_id = route.id)
            if not mobileUserRoutes:
                routesNotSet.append(route)

        return routesNotSet


def setRoute(request, num):
	context = RequestContext(request)
        routeId = -1 
        user_id = num

        routes = getNotSetRoutes(Route.objects.all())

        notSet = True
        _id = request.POST.get("set", "")
        if _id:
            routeId = request.POST.get("_id")
        
        if MobileUserRoute.objects.filter(route_id = routeId):
            notSet = False
        else:
            mobileUser = MobileUser.objects.get(pk=num)

        if _id:
            date = request.POST['date']
            if date:
                if not validate(date):
                    return HttpResponseRedirect('passDate' + str(num))
                route = Route.objects.get(pk=routeId)	
                mobileUserRoute = MobileUserRoute(route = route, mobileUser = mobileUser, date = date)
                mobileUserRoute.save()
                return HttpResponseRedirect('mobileUsersRoutes' + str(num))
            else:
                return HttpResponseRedirect('passDate' + str(num))

	else:
            if request.method == 'POST':
                Id = request.POST['Id']
                Name = request.POST['Name']

                if Name == None:
                    Name = r".*"
                if Id:
                    routes =  Route.objects.filter(pk = Id, name__regex=Name)
                else:
                    routes =  Route.objects.filter(name__regex=Name)
                    routes = getNotSetRoutes(routes)

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
                            if not validate(date):
                                return HttpResponseRedirect('passDate' + str(num))
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
                                mobileUsers =  MobileUser.objects.filter(pk = Id, username__regex=Login)
                            else:
                                mobileUsers =  MobileUser.objects.filter(username__regex=Login)

        routeId = num
	return render_to_response("setUserToRoute.html",
								locals(),
								context_instance=RequestContext(request))


def trackMobileUser(request, num):
	mobileUser = MobileUser.objects.get(pk=num)

	now = datetime.datetime.now().strftime("%Y-%m-%d") 
        routeQuery = "select * from \"mobileUsersRoutes_mobileuserroute\" where date = '" + now + "' and  \"mobileUser_id\" = '" + num +   "';"
	routes = MobileUserRoute.objects.raw(routeQuery)

	if len(list(routes)) != 0 :
		routeId = routes[0].trackingRoute_id
                
                if routeId:
                    routeName =  TrackingRoute.objects.filter(pk = routeId).values('name')[0]

                    lats = TrackingPoint.objects.filter(trackingRoute=routeId).values('latitude')
                    lons = TrackingPoint.objects.filter(trackingRoute=routeId).values('longitude')

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
    routeQuery = "select \"routes_route\".id, \"routes_route\".name from \"routes_route\" inner join \"mobileUsersRoutes_mobileuserroute\" on (\"routes_route\".id = \"mobileUsersRoutes_mobileuserroute\".\"route_id\") where \"mobileUsersRoutes_mobileuserroute\".\"mobileUser_id\" =" +str(num)+"; "
    routes = Route.objects.raw(routeQuery)
    mobileUserRoutesQuery = "select id, date from \"mobileUsersRoutes_mobileuserroute\" where \"mobileUsersRoutes_mobileuserroute\".\"mobileUser_id\" =" +str(num)+";"
    mobileUserRoutes = MobileUserRoute.objects.raw(mobileUserRoutesQuery)
    routesList = []
    mobileUserRoutesList = []

    for r in routes:
        routesList.append([r.id, r.name])
    for m in mobileUserRoutes:
        mobileUserRoutesList.append(m.date.strftime('%Y-%m-%d'))
    routesWithDate = dict(zip(mobileUserRoutesList, routesList)).items()
    return render_to_response("mobileUserHistory.html",
								locals(),
								context_instance=RequestContext(request))
