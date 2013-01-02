# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User
from django import forms

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

TYPE_ENT = (
    ( 'ROOT' , 'ROOT' ),
	( 'TIERS', 'TIERS'),
		)

class EntiteClass(models.Model):
	codent = models.CharField(_(u'Code Entite'),max_length=20, unique=True)
	noment = models.CharField(_(u'Nom Entite'),max_length=40)
	description = models.TextField(_(u'Description'))
	typent = models.CharField(_(u'Type Entite'), max_length=10, choices=TYPE_ENT )

	def __unicode__(self):
		return "%s : %s" % (self.codent, self.noment)

class UserProfile(models.Model):
    # This field is required.
	user = models.OneToOneField(User)
	tiers = models.ForeignKey(EntiteClass)

	def __unicode__(self):
		return "%s : %s" % (self.user, self.tiers)
