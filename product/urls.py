# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:33:10 2017

@author: Norbert
"""

from django.conf.urls import url

from . import views

app_name = 'product'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products/$', views.uploaddata, name='uploaddata'),
    url(r'^(?P<product_name>[\w\-]+)/$', views.detail, name='detail'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^user/register/$', views.register_user, name='register_user'),
    url(r'^user/login/$', views.login_user, name='login_user'),
]
