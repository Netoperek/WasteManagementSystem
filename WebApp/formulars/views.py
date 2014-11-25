# -*- coding: utf-8 -*-

from django.shortcuts import render
from points.models import Point
from formulars.models import Formular
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest

def formular(request, num):
	context = RequestContext(request)
	formulars = Formular.objects.filter(point_id = num)
	return render_to_response("formular.html",
								locals(),
								context_instance=RequestContext(request))
