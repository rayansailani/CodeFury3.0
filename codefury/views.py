
from django.http import HttpResponse
from django.shortcuts import render
from employment.models import Worker


def home(request):
    return render(request, 'home.html')


def dash(request):
    qauthor = request.user
    workers = Worker.objects.all().order_by('dateTime')
    # workers = workers.objects.filter(qauthor=user)
    context = {
        "workers": workers,
    }
    return render(request, 'dashboard.html', context)
