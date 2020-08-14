from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getanswer', views.getanswer, name='getanswer'),
]