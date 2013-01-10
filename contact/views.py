# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from dj1.util import get_pub_date, set_menu

from contact.models import Contact

BASE_RETOUR = '/contact/'

T_LISTE = 'Liste des Contacts'
T_MODIF = "Modification d'un contact"
T_CREATE = "Nouveau Contact"
T_ANNUL = "Annulation d'un Contact"

def populate(request):
	nb = 0
	for x in xrange(1,50):
		a = Contact()
		a.cod_contact = "COD%03d" % x
		a.nom_contact = "CONTACT No %03d" % x
		a.save()
		nb += 1

	return HttpResponse(" POPULATE OK %s " % nb)

		

## --------------
## Creation 
## --------------
def create(request, form, template):
	if request.method == 'POST':
		if request.POST['VALID'] == 'VALID':
			f = form(request.POST)
			if f.is_valid():
				f.save()
				return HttpResponseRedirect(BASE_RETOUR+'cr')
			## SI c'est pas valide ca repart
		else:
			## Bouton ANNUL
			return HttpResponseRedirect('/contact')
	else:
		f = form()

	return render( request, template, { 'form' : f, 'TITRE_PAGE':T_CREATE, 'PUB_DATE':get_pub_date() } ) 

## --------------
## Modification
## --------------
def modif(request, enreg_id, model, form, template):
	if request.method == 'POST':
		if request.POST['VALID'] == 'VALID':
			a = model.objects.get(id=enreg_id)
			f = form(request.POST, instance=a)
			if f.is_valid():
				f.save()
				return HttpResponseRedirect(BASE_RETOUR)
		else:
			## Bouton ANNUL
			return HttpResponseRedirect(BASE_RETOUR)
	else:
		a = model.objects.get(pk=enreg_id)
		f = form(instance=a)

	return render( request, template, { 'form' : f, 'TITRE_PAGE':T_MODIF, 'ENREG':enreg_id, 'PUB_DATE':get_pub_date() } )

## --------------
## Effacement
## --------------
def delete(request, enreg_id, model, template):
	if request.method == 'POST':
		if request.POST['VALID'] == 'VALID':
			a = model.objects.get(id=enreg_id).delete()
			return HttpResponseRedirect(BASE_RETOUR)
		else:
			## Bouton ANNUL
			return HttpResponseRedirect(BASE_RETOUR)
	else:
		obj = model.objects.get(pk=enreg_id)

	return render( request, template, { 'obj' : obj, 'TITRE_PAGE':T_ANNUL, 'PUB_DATE':get_pub_date() } )

## --------------------------------
## Liste Standard avec pagination
## --------------------------------
def liste(request, model, template, p=10):

	menu = set_menu( 'HOME', 'FX', 'TST', 'LOGOUT', 'ABOUT', 'CONTACT_US')
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

	return render_to_response(template, {'TITRE_PAGE':T_LISTE, "objs": objs, 'menu_items':menu, 'PUB_DATE':get_pub_date() })
