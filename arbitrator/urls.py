from django.urls import path

from django.urls import include
from .views import index_view, login_view, registration_view

app_name = 'arbitrator'

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='registration'),
]