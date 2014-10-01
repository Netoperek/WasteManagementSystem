from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest

def trackAll(request):
	context = RequestContext(request)
	return render_to_response("trackAll.html",
								locals(),
								context_instance=RequestContext(request))
