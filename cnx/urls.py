# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('cnx.views',
    # Examples:
    # url(r'^$', 'filex.views.home', name='home'),
    # url(r'^filex/', include('filex.foo.urls')),

	## cnx home => a voir
    #url(r'^$', 'index', name='index' ),
    url(r'^login/$', 'login_view', name='login' ),
    url(r'^logout/$', 'logout_view', name='logout' ),
	)
