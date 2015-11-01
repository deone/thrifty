from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^(?P<phone_number>\d+)/$', views.get, name='get'),
    url(r'^topup/$', views.topup, name='topup'),
    url(r'^pay/$', views.pay, name='pay'),
]
