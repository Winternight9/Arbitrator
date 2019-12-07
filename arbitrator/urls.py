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
from arbitrator.views import pollResultView
from arbitrator.views import myPollView
from arbitrator.views import changeResultAvailability
from arbitrator.views import changeVoteAvailability


app_name = 'arbitrator'

urlpatterns = [
    path('', indexView, name='index'),
    path('login/', loginView, name='login'),
    path('register/', registrationView, name='registration'),
    path('logout/', logoutView, name='logout'),
    path('home/', homeView, name='home'),
    path('profile/', profileView, name='profile'),
    path('profile/edit/', editProfileView, name='editProfile'),
    path('createPoll/', createPollView, name='createPoll'),
    path('poll/<int:poll_id>/', pollView, name='poll'),
    path('result/<int:poll_id>/', pollResultView, name='pollResult'),
    path('myPoll/', myPollView, name='myPoll'),
    path(
        'changeResultAvailability/',
        changeResultAvailability,
        name='changeResultAvailability'
    ),
    path(
        'changeVoteAvailability/',
        changeVoteAvailability,
        name='changeVoteAvailability'
    )
]
