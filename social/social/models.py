from django.db import models
from django.forms import ModelForm
from django import forms


class Activity(models.Model):


class Browse(models.Model):


class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=64)


class Upload(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.FileField()
