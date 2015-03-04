from django.shortcuts import render
from app.models import *
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html', {
       'navoptions': [('Go Home', '/home/')]
    })

def login(request):
    return render(request, 'login.html', {})


def about(request):
    return render(request, 'about.html', {})


def browse(request):
    return render(request, 'browse.html', {})


def activity(request):
    return render(request, 'activity.html', {})


def upload(request):
    return render(request, 'upload.html', {})