from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.home', name='home'),
	url(r'^mobileUsers$', 'mobileUsers.views.mobileUsers', name='mobileUsers'),
	url(r'^addMobileUser$', 'mobileUsers.views.addMobileUser', name='addMobileUser'),
	url(r'^routes$', 'routes.views.routes', name='routes'),
	url(r'^newRoute', 'map.views.newRoute', name='newRoute'),
	url(r'^routes', 'routes.views.routes', name='routes'),
	url(r'^routeDetails(?P<num>\d+)', 'routes.views.routeDetails', name='routeDetails'),
	url(r'^routeOnMap(?P<num>\d+)', 'routes.views.routeOnMap', name='routeOnMap'),
	url(r'^saveRoute/$','map.views.saveRoute'),
	url(r'^setRoute(?P<num>\d+)','routes.views.setRoute'),
	url(r'^mobileUsersRoutes(?P<num>\d+)','mobileUsers.views.mobileUsersRoutes'),
    url(r'^admin/', include(admin.site.urls)),
)
