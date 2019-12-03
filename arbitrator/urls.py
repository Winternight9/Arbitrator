from django.urls import path

from django.urls import include
from arbitrator.views import indexView
from arbitrator.views import loginView
from arbitrator.views import logoutView
from arbitrator.views import registrationView
from arbitrator.views import homeView
from arbitrator.views import profileView
from arbitrator.views import editProfileView
from arbitrator.views import createPollView
from arbitrator.views import pollView
from arbitrator.auth import createArbitratorUserFromGoogleAccount


app_name = 'arbitrator'

urlpatterns = [
    path('', indexView, name='index'),
    path('login/', loginView, name='login'),
    path('register/', registrationView, name='registration'),
    path('logout/', logoutView, name='logout'),
    path('home/', homeView, name='home'),
    path('profile/', profileView, name='profile'),
    path('profile/edit/', editProfileView, name='editProfile'),
    path(
        'createArbitratorUserFromGoogleAccount/',
        createArbitratorUserFromGoogleAccount,
        name='createArbitratorUserFromGoogleAccount'
    ),
    path('createPoll/', createPollView, name='createPoll'),
    path('poll/<int:poll_id>/', pollView, name='poll')
]