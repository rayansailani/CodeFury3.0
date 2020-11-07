from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm, CompanyForm
from employment.models import Worker
from django.contrib import messages

# Create your views here.


# def register(request):
#   if request.method == 'POST':
#      form = RegisterWorker(request.POST, request.FILES)
#     if form.is_valid():
#        # save article to db
#       instance = form.save(commit=False)
#      instance.user = request.user
#     instance.save()
#    # change this to the dashboard later
#   return redirect('/')
# else:
#   form = RegisterWorker()
# return render(request, 'employment/worker.html', {'form': form})


def register(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("home")

    return render(request, "employment/worker.html", {"form": form})


def regCompany(request):
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("home")

    return render(request, "employment/company.html", {"form": form})
