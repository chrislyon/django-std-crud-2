# -*- coding: utf-8 -*-
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template import Context, loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from django.db.models import Q

from dj1.util import get_pub_date, set_menu

from fx.models import FileXchange
from django.contrib.auth.models import User


@login_required(login_url='/cnx/login/')
def fx_home(request):
	t = 'fx/tmpl/index.html'
	titre = "FxChange MENU"
	menu = set_menu( 'HOME', 'FX', 'TST', 'LOGOUT', 'ABOUT' )
	USER = request.user

	return render_to_response(t, { 'menu_items':menu, 'USER':USER, 'TITRE_PAGE':titre, 'PUB_DATE':get_pub_date() })

## --------------------------------
## Upload a File
## --------------------------------
def fx_upload(request):

	T = "FILE(S) TO UPLOAD (User : %s)" % request.user
	menu = set_menu( 'HOME', 'FX', 'LOGOUT', 'ABOUT')
	template = 'fx/tmpl/fx_upload.html'
	
	obj_list = FileXchange.objects.filter(Q(from_user=request.user)|Q(to_user=request.user))

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

	return render_to_response(template, {'TITRE_PAGE':T, "objs": objs, 'menu_items':menu, 'PUB_DATE':get_pub_date() })


def fx_download(request):
	return HttpResponse("FX DOWNLOAD")

