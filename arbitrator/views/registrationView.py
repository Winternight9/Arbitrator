import sys

from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login
from arbitrator.forms import RegistrationForm
from django.contrib import messages
from arbitrator.models import ArbitratorUser


def registrationView(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)

            messages.success(request, f"Account: {username} created.\nWelcome to Arbitrator")

            return redirect(reverse("arbitrator:home"))
    else:
        form = RegistrationForm()

    context = {
        'form':  form
    }

    return render(request, 'arbitrator/registration.html', context)


sys.modules[__name__] = registrationView
