from django.urls import path

from django.urls import include
from .views import indexView, loginView, logoutView, registrationView, test, profileView, editProfileView, createPollView
from arbitrator.auth import createArbitratorUserFromGoogleAccount


app_name = 'arbitrator'

urlpatterns = [
    path('', indexView, name='index'),
    path('login/', loginView, name='login'),
    path('register/', registrationView, name='registration'),
    path('logout/', logoutView, name='logout'),
    path('test/', test, name='test'),
    path('profile/', profileView, name='profile'),
    path('profile/edit/', editProfileView, name='editProfile'),
    path(
        'createArbitratorUserFromGoogleAccount',
        createArbitratorUserFromGoogleAccount,
        name='createArbitratorUserFromGoogleAccount'
    ),
    path('createPoll', createPollView, name='createPoll')
]