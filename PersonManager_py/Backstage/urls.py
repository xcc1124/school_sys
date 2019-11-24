#!_*_coding:utf-8_*_
#__author__:"Xiao CC"
from django.conf.urls import url
from Backstage import views

urlpatterns=[
    url(r'^/$', views.index),
    url(r'login.this/$',views.login),
    url(r'CAPTCHA/$',views.CAPTCHA),
    url(r'test/$',views.test),
    url(r'log_out/$',views.log_out),
    url(r'update_user/$',views.update_user),
]