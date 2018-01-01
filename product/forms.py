# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 21:28:42 2017

@author: Norbert
"""

from django import forms

class RegisterForm(forms.Form):
    reg_username = forms.CharField(label='Username', max_length=10)
    reg_email = forms.EmailField(label='E-mail address')
    reg_password = forms.CharField(label='Password', max_length=15)
    
class LoginForm(forms.Form):
    log_username = forms.CharField(label='Username',max_length=10)
    log_password = forms.CharField(label='Password')

class UploadForm(forms.Form):
    uploadfile = forms.FileField(label='Select file')