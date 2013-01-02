# -*- coding: utf-8 -*-
# Create your views here.


from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login

from django.forms.util import ErrorList
from cnx.forms import LoginForm

from dj1.util import set_menu, get_pub_date


def login_view(request):
	menu = set_menu( 'HOME', 'ABOUT', 'CONTACT_US' )
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				# Redirect to a success page.
				return HttpResponseRedirect('/tst')
			else:
				form._errors["username"] = ErrorList([u"Acces Denied"])
		else:
			form._errors["username"] = ErrorList([u"Acces Denied"])
			return HttpResponseRedirect('/cnx/login')
	else:
		form = LoginForm()

	return render( request, 'cnx/tmpl/login.html', { 'form' : form, 'menu_items':menu } )


def logout_view(request):
	menu = set_menu( 'HOME', 'ABOUT', 'CONTACT_US' )
	if request.method == 'POST':
		if request.POST["VALID"] == "OK":
			# Bouton VALID
			logout(request)
			return render( request, 'cnx/tmpl/logout_confirm.html', 
				{ 'menu_items':menu , 'PUB_DATE': get_pub_date(), 'TITRE_PAGE': "DECONNEXION CONFIRMEE" }, )
		else:
			## ici on pourrait peut faire un retour arriere
			return HttpResponseRedirect('/')
	else:
		pass
	return render( request, 'cnx/tmpl/logout.html', { 'menu_items':menu , 'PUB_DATE':get_pub_date(), 'TITRE_PAGE':"DECONNEXION"} )
