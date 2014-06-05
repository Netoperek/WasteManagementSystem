from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from .forms import MobileUserForm
from mobileUsers.models import MobileUser

from routes.models import Route
# Create your views here.

def mobileUsers(request):
	mobileUsers = MobileUser.objects.all()
	
	_id = request.POST.get("remove", "")
	if _id:
		MobileUser.objects.filter(id=int(_id.split(' ')[2])).delete()

	else:
		if request.method == 'POST':
			Id = request.POST['id']
			Login = request.POST['Login']

			if Login == None:
				Login = r".*"

			if Id:
				mobileUsers =  MobileUser.objects.filter(pk = Id,
														login__regex=Login)
			else:
				mobileUsers =  MobileUser.objects.filter(login__regex=Login)

	return render_to_response("mobileUsers.html",
								locals(),
								context_instance=RequestContext(request))

def addMobileUser(request):

	form = MobileUserForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('mobileUsers')

	return render_to_response("addMobileUser.html",
								locals(),
								context_instance=RequestContext(request))

def mobileUsersRoutes(request, num):
	_id = request.POST.get("unset", "")
	if _id:
		route = Route.objects.get(id=int(_id.split('#')[1]))
		print route
		route.save()

	query = 'select routes_route.id, routes_route.name from routes_route inner join "mobileUsersRoutes_mobileuserroute" on (routes_route.id = "mobileUsersRoutes_mobileuserroute".route_id) where "mobileUsersRoutes_mobileuserroute"."mobileUser_id" =' +str(num)+' ;'

	routes = Route.objects.raw(query)
	return render_to_response("mobileUsersRoutes.html",
								locals(),
								context_instance=RequestContext(request))