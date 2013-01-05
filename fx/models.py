# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from Utilis.models import UserProfile, EntiteClass

FX_STATUS = (
	( 'INIT', 'INITIAL'),
	( 'UP', 'UPLOADED' ),
	( 'DOWN', 'DOWNLOADED'),
	( 'END', 'TERMINE'),
)

FX_SENS = (
	( 'EMIS' , 'Emission' ),
	( 'RECV',	'Reception'),
)

class FileXchange(models.Model):
	cod_fx = models.CharField(_(u'Code Fx'),max_length=20, unique=True)
	nom_fx = models.CharField(_(u'Nom Fx'),max_length=40)
	description = models.TextField(_(u'Description'), blank=True)
	fx_sens = models.CharField(_(u'Sens Fx'),max_length=5, choices=FX_SENS, default='RECV')
	from_user = models.ForeignKey(UserProfile, related_name='+')
	to_user = models.ForeignKey(UserProfile, related_name='+')
	fx_status = models.CharField(_(u'Status Fx'),max_length=10, choices=FX_STATUS, default='INIT')
	Original_name = models.CharField(_(u'Nom Origine'),max_length=40, blank=True)
	Destination_name = models.CharField(_(u'Nom Destination'),max_length=40, blank=True)
	fx_field = models.FileField(upload_to='fichiers/%Y/%m/%d', blank=True)

	def __unicode__(self):
		return "%s : %s [ %s | %s ]" % (self.cod_fx, self.nom_fx, self.fx_sens, self.fx_status)

	@property
	def from_user_list_name(self):
		t = self.from_user.tiers.noment
		u = self.from_user.user.username
		return "%s : %s" % (u,t)

	@property
	def to_user_list_name(self):
		t = self.to_user.tiers.noment
		u = self.to_user.user.username
		return "%s : %s" % (u,t)

class FxForm(ModelForm):
	class Meta:
		model = FileXchange
