from django.urls import path

from .views import indexView,logoutView


app_name = 'arbitrator'
urlpatterns = [
    path('',indexView, name='index'),
    path('login/',indexView, name='login'),
    path('logout/',logoutView, name='logout'),
]