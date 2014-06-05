from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.forms import UserCreationForm
from .forms import WebAppUserForm
from django.contrib.auth.models import User


def addWebUser(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			HttpResponseRedirect('/webAppUsers/')
	else:
		form = UserCreationForm(request.POST)

	return render_to_response("addWebUser.html",
								locals(),
								context_instance=RequestContext(request))

def webAppUsers(request):
	webUsers = User.objects.all()

	_id = request.POST.get("remove", "")
	if _id:
		User.objects.filter(id=int(_id.split(' ')[2])).delete()

	else:
		if request.method == 'POST':
			Id = request.POST['id']
			Login = request.POST['username']

			if Login == None:
				Login = r".*"

			if Id:
				webUsers =  User.objects.filter(pk = Id,
												username__regex=Login)
			else:
				webUsers =  User.objects.filter(username__regex=Login)

	return render_to_response("webUsers.html",
								locals(),
								context_instance=RequestContext(request))