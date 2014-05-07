from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from mobileUsers.models import MobileUser
from routes.models import Route
from mobileUsersRoutes.models import MobileUserRoute
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
		mobileUserRoute = MobileUserRoute(route = route, mobileUser = mobileUser, date = date)
		mobileUserRoute.save()
		return HttpResponseRedirect('mobileUsers')

	return render_to_response("setRoute.html",
								locals(),
								context_instance=RequestContext(request))