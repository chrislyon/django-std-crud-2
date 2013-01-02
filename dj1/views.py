# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from dj1.util import get_pub_date, set_menu

### POUR TEST
def hello(request):
    return HttpResponse("Hello, world.")

def about(request):
	menu = set_menu( 'HOME', 'ABOUT', 'CONTACT_US' )
	T = "A propos"
	return render_to_response('tmpl/about.html', {'TITRE_PAGE':T, 'menu_items' : menu , 'PUB_DATE':get_pub_date() })

def contact_us(request):
	menu = set_menu( 'HOME', 'ABOUT', 'CONTACT_US' )
	T = "Contactez Nous"
	return render_to_response('tmpl/contact_us.html', {'TITRE_PAGE':T, 'menu_items' : menu, 'PUB_DATE':get_pub_date() })

def index(request):
	t = 'tmpl/index.html'
	if request.user.is_authenticated():
		titre = "WELCOME %s" % request.user
		USER = request.user
		menu = set_menu( 'HOME', 'TST', 'LOGOUT', 'ABOUT', 'CONTACT_US' )
	else:
		titre = "WELCOME"
		USER = None
		menu = set_menu( 'HOME', 'LOGIN', 'ABOUT', 'CONTACT_US' )

	return render_to_response(t, { 'menu_items':menu, 'USER':USER, 'TITRE_PAGE':titre, 'PUB_DATE':get_pub_date() })

