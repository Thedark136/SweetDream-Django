from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    # return HttpResponse('Hello world!')
    return render(request, 'home.html')

def recrutements_view(request):
    # return HttpResponse('Contactez nous')
    return render(request, 'recrutements.html')

def ally_truces_view(request):
    return render(request, 'ally_truces.html')