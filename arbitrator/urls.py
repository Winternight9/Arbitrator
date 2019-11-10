from django.urls import path

from django.urls import include
from .views import indexView, loginView, logoutView, registrationView, test
from arbitrator.auth import createArbitratorUserFromGoogleAccount


app_name = 'arbitrator'

urlpatterns = [
    path('', indexView, name='index'),
    path('login/', loginView, name='login'),
    path('register/', registrationView, name='registration'),
    path('logout/', logoutView, name='logout'),
    path('test/', test, name='test'),
    path(
        'createArbitratorUserFromGoogleAccount',
        createArbitratorUserFromGoogleAccount,
        name='createArbitratorUserFromGoogleAccount'
    )
]