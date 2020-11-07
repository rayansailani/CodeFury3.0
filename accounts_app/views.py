from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomRegistration

# Create your views here.


def homepage(request):
    return render(
        request,
        "home.html",
    )


def register(request):
    if request.method == "POST":
        register_form = CustomRegistration(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "NEW   user ACCOUNT CREAted")
            return redirect("register")
    else:

        register_form = CustomRegistration()
    return render(request, "register.html", {"register_form": register_form})
