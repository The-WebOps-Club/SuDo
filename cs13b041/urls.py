from django.conf.urls.defaults import patterns, include, url
from app1.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
   	url(r'^$',home),
    	url(r'^app1/$',hello ),
	url(r'^time/$',time),
	url(r'^login/$', login_form),
	url(r'^submit/$', submit),
	
    # Uncomment the admin/doc line below to enable admin documentation:
     	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    	url(r'^admin/', include(admin.site.urls)),
)
