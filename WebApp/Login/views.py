from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginWebAppUser(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/")
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			return HttpResponseRedirect("invalidLogin.html")
	else:
		return render_to_response("loginPage.html",
								locals(),
								context_instance=RequestContext(request))

def invalidLogin(request):
	return render_to_response("invalidLogin.html",
								locals(),
								context_instance=RequestContext(request))


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("home.html")

