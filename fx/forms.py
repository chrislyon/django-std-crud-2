# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
	docfile = forms.FileField( label='Choisissez un fichier', help_text='max. 42 megabytes' )
