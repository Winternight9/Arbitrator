import sys

from django.shortcuts import render, redirect,reverse
from django.contrib.auth.models import User
from arbitrator.forms import EditProfileForm

def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance =request.user)

        if form.is_valid():
            form.save()

            return redirect(reverse("arbitrator:profile"))
    else:
        form = EditProfileForm(instance =request.user)
        args = {'form' : form}

        return render(request, 'arbitrator/editProfile.html', args)        
 

sys.modules[__name__] = editProfile
