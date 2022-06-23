from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse

from .forms import SignupForm


def signup(request):
    status = 200

    if request.user.is_authenticated:
        return redirect(reverse('landing'))

    if request.method == "POST":
        # `is_active` default at True because
        # there's no email verification currently.
        form = SignupForm(request.POST, initial={"is_active": True})

        if form.is_valid():
            user = form.save()

            login(request, user)  # Log in the new user.

            return redirect(reverse('landing'))
        else:
            # Validation error append
            status = 400
    else:
        form = SignupForm()

    ctx = {"form": form}

    return render(request, 'accounts/signup.html', context=ctx, status=status)
