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

def acCare(request):
    return render(request, 'ac-care.html')

def services(request):
    return render(request, 'all-services.html')