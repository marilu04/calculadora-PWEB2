from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('soma', views.Soma, name='soma'),
]