from django.urls import path

from .views import indexView


app_name = 'arbitrator'
urlpatterns = [
    path('',indexView, name='index'),


]