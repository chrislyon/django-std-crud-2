# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from tst.models import Contact, ContactForm

urlpatterns = patterns('tst.views',
    # Examples:
    # url(r'^$', 'filex.views.home', name='home'),
    # url(r'^filex/', include('filex.foo.urls')),

	## Url standard 
	url(r'^$', 'std_liste', { 'model':Contact, 'template':'tst/tmpl/liste.html', 'p':5, }, name='tst_liste'),
	url(r'^cr/$', 'tst_create', { 'form':ContactForm, 'template':'tst/tmpl/tst_form.html', }, name='tst_cr'),
	url(r'^mo/(\d+)$', 'tst_modif', { 'model':Contact, 'form':ContactForm, 'template':'tst/tmpl/tst_form.html', }, name='tst_mo'),
	url(r'^del/(\d+)/$', 'tst_delete', { 'model':Contact, 'template':'tst/tmpl/tst_delete.html', }, name='tst_del'),
	)
