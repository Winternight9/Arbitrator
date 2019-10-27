from django.urls import path

from . import views


app_name = 'arbitrator'
urlpatterns = [
    path('',views.indexview, name='index'),


]