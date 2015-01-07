from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from points.models import Point
from routes.models import Route
from address.models import Address

def newRoute(request):
    return render_to_response("newRoute.html",
                                locals(),
                                context_instance=RequestContext(request))
def getLatitude(point):
    print "getLatitude"
    print float(point.split('#')[0])
    return float(point.split('#')[0])

def getLongitude(point):
    print "getLongitude"
    print float(point.split('#')[1])
    return float(point.split('#')[1])

def getAddress(point):
    print "getAddress"
    print point.split('#')[2]
    return point.split('#')[2]

def getStreet(address):
    print "getStreet"
    i = getNumberPos(address)
    split_addr = address[:i]
    result = " ".join(split_addr)
    print result
    return result

def getNumberPos(address):
    i = 0
    while i < len(address):
        if address[i].replace(",","").isdigit():
            break
        i = i + 1

    return i


def getNumber(address):
    print "getNumber"
    i = getNumberPos(address)
    print address[i].replace(",","")
    return address[i].replace(",","")

def getCode(address):
    print "getCode"
    i = getNumberPos(address) + 1
    print address[i].replace(",","")
    return address[i].replace(",","")

def getCity(address):
    print "getCity"
    i = getNumberPos(address) + 2
    print address[i].replace(",","")
    return address[i].replace(",","")

def saveRoute(request):
    points = []
    if request.POST.has_key('points'):
        points = request.POST.getlist('points')
        routeName =  request.POST.get('routeName')
        route = Route(name = routeName)
        route.save()

        for point in points:
            print "KURWA TU"
            print point
            address = getAddress(point).split(' ')[1:]
            saveAddress = Address(street = getStreet(address), number = getNumber(address), postCode = getCode(address), city = getCity(address))
            saveAddress.save()
            savePoint = Point(route = route, address = saveAddress, longitude = getLongitude(point), latitude = getLatitude(point))
            savePoint.save()
        return HttpResponse('Trasa zapisana')

    return HttpResponse('Wybierz conajmniej jeden punkt')
