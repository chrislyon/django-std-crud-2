# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from contact.models import Contact, ContactForm

BASE_TMPL='contact/tmpl'

urlpatterns = patterns('contact.views',
	## Url standard 
	url(r'^$', 'liste', { 'model':Contact, 'template':BASE_TMPL+'/liste.html', 'p':10, }, name='liste'),
	url(r'^cr/$', 'create', { 'form':ContactForm, 'template':BASE_TMPL+'/form.html', }, name='cr'),
	url(r'^mo/(\d+)$', 'modif', { 'model':Contact, 'form':ContactForm, 'template':BASE_TMPL+'/form.html', }, name='mo'),
	url(r'^del/(\d+)/$', 'delete', { 'model':Contact, 'template':BASE_TMPL+'/delete.html', }, name='del'),
	#url(r'^pop$', 'populate', name='pop'),
	)
