
from django.http import HttpResponse
from django.shortcuts import render
from employment.models import Worker, Listing


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


def listing(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'listing.html', context)
