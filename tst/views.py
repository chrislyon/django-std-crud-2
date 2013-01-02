# -*- coding: utf-8 -*-
# Create your views here.
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import CreateView, UpdateView, DeleteView

from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from dj1.util import get_pub_date, set_menu
from tst.models import Contact, ContactForm

@login_required(login_url='/login/')
def index(request):
	return HttpResponse(" OK ")

## --------------
## Creation 
## --------------
@login_required(login_url='/cnx/login/')
def tst_create(request):
	if request.method == 'POST':
		if request.POST['VALID'] == 'VALID':
			f = ContactForm(request.POST)
			if f.is_valid():
				f.save()
				return HttpResponseRedirect('/tst/cr')
			## SI c'est pas valide ca repart
		else:
			## Bouton ANNUL
			return HttpResponseRedirect('/tst')
	else:
		f = ContactForm()

	return render( request, 'tst/tmpl/tst_form.html', { 'form' : f, 'TITRE_PAGE':'NOUVEAU CONTACT', 'PUB_DATE':get_pub_date() } ) 

## --------------
## Modification
## --------------
@login_required(login_url='/cnx/login/')
def tst_modif(request, enreg_id):
	if request.method == 'POST':
		if request.POST['VALID'] == 'VALID':
			a = Contact.objects.get(id=enreg_id)
			f = ContactForm(request.POST, instance=a)
			if f.is_valid():
				f.save()
				return HttpResponseRedirect('/tst')
		else:
			## Bouton ANNUL
			return HttpResponseRedirect('/tst')
	else:
		a = Contact.objects.get(pk=enreg_id)
		f = ContactForm(instance=a)

	return render( request, 'tst/tmpl/tst_form.html', { 'form' : f, 'TITRE_PAGE':'MODIFICATION CONTACT', 'ENREG':enreg_id, 'PUB_DATE':get_pub_date() } )

## --------------
## Effacement
## --------------
@login_required(login_url='/cnx/login/')
def tst_delete(request, enreg_id):
	if request.method == 'POST':
		if request.POST['VALID'] == 'VALID':
			a = Contact.objects.get(id=enreg_id).delete()
			return HttpResponseRedirect('/tst')
		else:
			## Bouton ANNUL
			return HttpResponseRedirect('/tst')
	else:
		obj = Contact.objects.get(pk=enreg_id)

	return render( request, 'tst/tmpl/tst_delete.html', { 'obj' : obj, 'TITRE_PAGE':'ANNULATION CONTACT', 'PUB_DATE':get_pub_date() } )

## --------------------------------
## Liste Standard avec pagination
## --------------------------------
@login_required(login_url='/cnx/login/')
def std_liste(request, model, template, base_href, p=10):

	T = "LISTE DES CONTACTS"
	menu = set_menu( 'HOME', 'TST', 'LOGOUT', 'ABOUT', 'CONTACT_US')
	obj_list = model.objects.all()
	paginator = Paginator(obj_list, p)

	page = request.GET.get('page')
	try:
		objs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		objs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		objs = paginator.page(paginator.num_pages)

	return render_to_response(template, {'TITRE_PAGE':T, "objs": objs, 'B_HREF':base_href, 'menu_items':menu, 'PUB_DATE':get_pub_date() })

