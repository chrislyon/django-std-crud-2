# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from fx.models import FileXchange

urlpatterns = patterns('fx.views',
    # Examples:
    # url(r'^$', 'filex.views.home', name='home'),
    # url(r'^filex/', include('filex.foo.urls')),

	## Url Fx
	url(r'^$', 'fx_home', name='fx_home'),
	url(r'^upload$', 'fx_upload', name='fx_upload'),
	url(r'^up/(\d+)$', 'fx_up', name='fx_up'),
	url(r'^do/(\d+)$', 'fx_do', name='fx_do'),
	url(r'^download$', 'fx_download', name='fx_download'),
	)
