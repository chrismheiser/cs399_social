from django.shortcuts import render
from app.models import *
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html', {
       'navoptions': [('Go Home', '/home/')]
    })
