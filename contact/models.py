# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm

from django.utils.translation import ugettext_lazy as _

TYPE_CONTACT = (
	( 'PRO', 'PROFESSIONEL'),
	( 'PERSO', 'PERSONNEL' ),
	( 'VIP', 'VIP'),
	( 'AUTRE', 'AUTRE'),
)

# Create your models here.
class Contact(models.Model):
	cod_contact = models.CharField(_(u'Code Contact'),max_length=20, unique=True)
	nom_contact = models.CharField(_(u'Nom Contact'),max_length=40)
	description = models.TextField(_(u'Description'))
	tel_contact = models.CharField(_(u'Téléphone'), max_length=30)
	typ_contact = models.CharField(_(u'Type Contact'), max_length=10, choices=TYPE_CONTACT, default='PRO' )

	def __unicode__(self):
		return "%s : %s" % (self.cod_contact, self.nom_contact)

class ContactForm(ModelForm):
	class Meta:
		model = Contact
