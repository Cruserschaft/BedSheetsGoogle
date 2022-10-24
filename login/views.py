from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *


def user_login(request):
    form = LoginForm(request.POST or None)
    next_get = request.GET.get("next")
    context = {"login_form": form}

    if request.user.is_authenticated:
        username = request.user.username
        context["username"] = username

    if form.is_valid():
        username, password = request.POST.get("username"), request.POST.get("password"),
        user = authenticate(username=username, password=password)
        if not user:
            return redirect(request.META.get("HTTP_REFERER"))
        login(request, user)
        next_post = request.POST.get("next")
        return redirect(next_get or next_post or "/")

    return render(request, "login.html", context=context)


def user_register(request):
    form = RegistrationUserForm(request.POST or None)
    context = {"reg": form, }

    if request.user.is_authenticated:
        username = request.user.username
        context["username"] = username

    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data["password"])
        new_user.save()
        return redirect("/login", context={'username': new_user})

    return render(request, 'register.html', context=context)


def user_logout(request):
    logout(request)
    return redirect("/")
