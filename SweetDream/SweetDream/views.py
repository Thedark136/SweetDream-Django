from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RCForm
from . import models
from django import forms 

def home_view(request):
    # return HttpResponse('Hello world!')
    return render(request, 'home.html')

def recrutements_view(request):
    submitted = False
    if request.method == "POST":
        form = RCForm()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = RCForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'recrutements.html',{'form': form})

def ally_truces_view(request):
    return render(request, 'ally_truces.html')