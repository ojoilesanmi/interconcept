from django.urls import path

from . import views

from django.conf import settings

urlpatterns = [

    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('team', views.team, name='team'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services')

]