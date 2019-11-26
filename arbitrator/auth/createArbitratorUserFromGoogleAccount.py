import sys

from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from arbitrator.models import ArbitratorUser


@login_required
def createArbitratorUserFromGoogleAccount(request):
    user = request.user

    try:
        existing_user = ArbitratorUser.objects.get(user=user)

        messages.success(request, f"{request.user.email} SignIn complete.\nWelcome to Arbitrator")

        return redirect(reverse("arbitrator:home"))

    except ArbitratorUser.DoesNotExist:
        new_user = ArbitratorUser(user=user)
        new_user.save()

        messages.success(request, f"Account: {request.user.email} created.\nWelcome to Arbitrator")

        return redirect(reverse("arbitrator:home"))


sys.modules[__name__] = createArbitratorUserFromGoogleAccount
