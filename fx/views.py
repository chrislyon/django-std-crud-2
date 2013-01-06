# -*- coding: utf-8 -*-
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.core.servers.basehttp import FileWrapper

from django.template import Context, loader
from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from django.db.models import Q

from dj1.util import get_pub_date, set_menu

from fx.models import FileXchange
from fx.forms import DocumentForm
from django.contrib.auth.models import User

from StringIO import StringIO
import os, mimetypes, urllib

@login_required(login_url='/cnx/login/')
def fx_home(request):
	t = 'fx/tmpl/index.html'
	titre = "FxChange MENU"
	menu = set_menu( 'HOME', 'FX', 'TST', 'LOGOUT', 'ABOUT' )
	USER = request.user

	return render_to_response(t, { 'menu_items':menu, 'USER':USER, 'TITRE_PAGE':titre, 'PUB_DATE':get_pub_date() })

## ----------------------
## Formulaire d'upload
## Permet d'uploader un fichier
## ----------------------
def fx_up(request, fx_id):
	P = get_pub_date()
	template = 'fx/tmpl/fx_up_form.html'
	fich = FileXchange.objects.get(pk=fx_id)
	T = 'UPLOAD A FILE : %s' % fich.nom_fx
	if request.method == 'POST':
		if request.POST['VALID'] == 'VALID':
			f = DocumentForm(request.POST, request.FILES)
			if f.is_valid():
				fich = FileXchange.objects.get(pk=fx_id)
				fich.fx_status = 'UP'
				fich.fx_field = request.FILES['docfile']
				fich.save()
				return HttpResponseRedirect('/fx/upload')
		else:
			## Bouton ANNUL
			return HttpResponseRedirect('/fx/upload')
	else:
		f = DocumentForm()

	return render_to_response( template, { 'form' : f, 'TITRE_PAGE':T, 'PUB_DATE':P }, context_instance=RequestContext(request))


## --------------------------------
## Liste des fichiers a uploader
## --------------------------------
def fx_upload(request):

	T = "FILE(S) TO UPLOAD (User : %s)" % request.user
	menu = set_menu( 'HOME', 'FX', 'LOGOUT', 'ABOUT')
	template = 'fx/tmpl/fx_list.html'
	TL = "UPLOAD"
	
	obj_list = FileXchange.objects.filter(from_user=request.user)

	## Pagination 
	paginator = Paginator(obj_list, 5)
	page = request.GET.get('page')
	try:
		objs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		objs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		objs = paginator.page(paginator.num_pages)

	return render_to_response(template, {'UPLOAD':True, 'TITRE_PAGE':T, "objs": objs, 'menu_items':menu, 'PUB_DATE':get_pub_date() })

## --------------------------------
## Liste des fichiers a Downloader
## --------------------------------
def fx_download(request):

	T = "FILE(S) TO DOWNLOAD (User : %s)" % request.user
	menu = set_menu( 'HOME', 'FX', 'LOGOUT', 'ABOUT')
	template = 'fx/tmpl/fx_list.html'
	TL = "DOWNLOAD"
	
	obj_list = FileXchange.objects.filter(to_user=request.user)

	## Pagination 
	paginator = Paginator(obj_list, 5)
	page = request.GET.get('page')
	try:
		objs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		objs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		objs = paginator.page(paginator.num_pages)

	return render_to_response(template, {'UPLOAD':False, 'TITRE_PAGE':T, "objs": objs, 'menu_items':menu, 'PUB_DATE':get_pub_date() })

## ----------------
## Download a File
## ----------------
def fx_do(request, fx_id):
	fich = FileXchange.objects.get(pk=fx_id)
	fich.fx_status = 'DOWN'
	fich.save()
	data = StringIO(file(fich.fx_field.path, "rb").read())
	response = HttpResponse(data, content_type="binary/octet-stream")
	response['Content-Disposition'] = 'attachment; filename=%s' % "FICHIER.DATA"
	return response
