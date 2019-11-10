import sys

from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from ..forms import LoginForm


def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect(reverse("arbitrator:test"))
        else:
            messages.error(request, f"Username or password is not valid")

    form = LoginForm()
    context = {
        'form':  form
    }

    return render(request, 'arbitrator/login.html', context)


sys.modules[__name__] = loginView