from django.urls import path

from django.urls import include
from .views import indexView, loginView, logoutView, registrationView, homeView, profileView, editProfileView, createPollView


app_name = 'arbitrator'

urlpatterns = [
    path('', indexView, name='index'),
    path('login/', loginView, name='login'),
    path('register/', registrationView, name='registration'),
    path('logout/', logoutView, name='logout'),
    path('home/', homeView, name='home'),
    path('profile/', profileView, name='profile'),
    path('profile/edit/', editProfileView, name='editProfile'),
    path('createPoll', createPollView, name='createPoll')
]