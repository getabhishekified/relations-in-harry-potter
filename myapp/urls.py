from django.urls import path
from django.views.generic.base import RedirectView
from . import views

favicon_view = RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)

urlpatterns = [
    path('/', views.groot, name='/')
    path('', views.index, name='index'),
    path('getanswer', views.getanswer, name='getanswer'),
    path('favicon\.ico', favicon_view)
]