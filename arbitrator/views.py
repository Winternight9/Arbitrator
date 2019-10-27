from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.utils import timezone 
from django.views import generic
from django.contrib import messages


def indexview(request):
    return render(request, 'arbitrator/index.html')
    
    
