from django.urls import path

from django.urls import include
from .views import indexView, loginView, registrationView,test
from .views import indexView,logoutView


app_name = 'arbitrator'

urlpatterns = [
    path('', indexView, name='index'),
    path('login/', loginView, name='login'),
    path('register/', registrationView, name='registration'),
    path('logout/',logoutView, name='logout'),
    path('test/', test, name='test'),
]