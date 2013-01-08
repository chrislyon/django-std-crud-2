# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from contact.models import Contact, ContactForm

urlpatterns = patterns('contact.views',
	## Url standard 
	url(r'^$', 'liste', { 'model':Contact, 'template':'contact/tmpl/liste.html', 'p':5, }, name='liste'),
	url(r'^cr/$', 'create', { 'form':ContactForm, 'template':'contact/tmpl/form.html', }, name='cr'),
	url(r'^mo/(\d+)$', 'modif', { 'model':Contact, 'form':ContactForm, 'template':'tst/tmpl/form.html', }, name='mo'),
	url(r'^del/(\d+)/$', 'delete', { 'model':Contact, 'template':'tst/tmpl/delete.html', }, name='del'),
	)
