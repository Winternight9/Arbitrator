from django.urls import path

from django.urls import include
from .views import indexView, loginView, logoutView, createStatistic, registrationView, test


app_name = 'arbitrator'

urlpatterns = [
    path('', indexView, name='index'),
    path('login/', loginView, name='login'),
    path('register/', registrationView, name='registration'),
    # path('stat/',createStatistic, name='login'),
    path('logout/', logoutView, name='logout'),
    path('test/', test, name='test'),
]
