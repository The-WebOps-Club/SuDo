#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from tuts.views import *
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required, permission_required

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sudo.views.home', name='home'),
    url(r'^users/.*$',RedirectView.as_view(url=settings.SITE_URL,permanent=False)),
    url(r'^tuts/', login_required(FileListView.as_view()), name='tuts'),
    url(r'^attend/$', 'sudo.views.attend', name='attend'),
    url(r'^gistsubmit/', 'sudo.views.gistsubmit', name='gistsubmit'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^sudo/', include('sudo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.static', (r'^static/(?P<path>.*)$'
                        , 'serve',
                        {'document_root': settings.STATIC_ROOT,
                        'show_indexes': True}))

urlpatterns += patterns('django.views.static', (r'^media/(?P<path>.*)$'
                        , 'serve',
                        {'document_root': settings.MEDIA_ROOT,
                        'show_indexes': True}))