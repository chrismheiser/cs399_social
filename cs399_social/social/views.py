from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


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