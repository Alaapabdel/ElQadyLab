from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ar', views.indexar, name='indexar'),
    path('contactus', views.contactus, name='contactus'),
    path('contactusar', views.contactusar, name='contactusar'),
    path('service', views.service, name='service'),
    path('servicear', views.servicear, name='servicear'),
    path('option', views.option, name='option'),
    path('optionar', views.optionar, name='optionar'),
    path('values', views.values, name='values'),
    path('valuesar', views.valuesar, name='valuesar'),
]
