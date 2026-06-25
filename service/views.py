from django.shortcuts import render
from accounts.models import ServiceProvider


def engineers(request):

    engineers = ServiceProvider.objects.filter(
        service="AC Repair Service"
    )

    return render(
        request,
        'ac-engineers.html',
        {
            'engineers': engineers
        }
    )
def barbers(request):

    barbers = ServiceProvider.objects.filter(
        service="Hair Care Service"
    )

    return render(
        request,
        'barber.html',
        {
            'barbers': barbers
        }
    )
def beauticians(request):

    beauticians = ServiceProvider.objects.filter(
        service="Beauty Service"
    )

    return render(
        request,
        'beautician.html',
        {
            'beauticians': beauticians
        }
    )
def therapists(request):

    therapists = ServiceProvider.objects.filter(
        service="Spa Service"
    )

    return render(
        request,
        'therapist.html',
        {
            'therapists': therapists
        }
    )

def cleaners(request):

    cleaner = ServiceProvider.objects.filter(
        service="Cleaning Service"
    )

    return render(
        request,
        'cleaning-engineers.html',
        {
            'cleaners': cleaners
        }
    )

def plumbers(request):

    plumbers = ServiceProvider.objects.filter(
        service="Plumbing Service"
    )

    return render(
        request,
        'plumbing-engineers.html',
        {
            'plumbers': plumbers
        }
    )

def acCare(request):
    return render(request, 'ac-care.html')

def services(request):
    return render(request, 'all-services.html')