from django.urls import path

from .views import indexView,logoutView,create_statistic,homePage


app_name = 'arbitrator'
urlpatterns = [
    path('',indexView, name='index'),
    path('homepage/',homePage,name='home'),
    path('stat/',create_statistic, name='login'),
    path('logout/',logoutView, name='logout'),
]