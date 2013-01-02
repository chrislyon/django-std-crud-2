# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from tst.models import Contact

urlpatterns = patterns('tst.views',
    # Examples:
    # url(r'^$', 'filex.views.home', name='home'),
    # url(r'^filex/', include('filex.foo.urls')),

	url(r'^$', 'std_liste', { 'model':Contact, 'template':'tst/tmpl/liste.html', 'base_href':'/tst', 'p':8,  }, name='tst_liste'),
	url(r'^cr/$', 'tst_create', name='tst_cr'),
	url(r'^mo/(\d+)$', 'tst_modif', name='tst_mo'),
	url(r'^del/(\d+)/$', 'tst_delete', name='tst_del'),
	)
