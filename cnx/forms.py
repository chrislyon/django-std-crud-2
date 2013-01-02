# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='Code Utilisateur',max_length=20)
	password = forms.CharField(label='Mot de passe',max_length=20, widget=forms.PasswordInput)

#	def clean(self):
#		cleaned_data = super(LoginForm, self).clean()
#		user = cleaned_data.get("user")
#		user = User.objects.filter(username=user)
#		if not user.exists():
#			raise forms.ValidationError("User does not exists")
#		if not user.is_active:
#			raise forms.ValidationError("This account is not active")
