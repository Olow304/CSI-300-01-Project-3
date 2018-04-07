from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate, logout
from django import template
from django.urls import reverse

# Create your views here.
def home_page(request):
    return render(request, 'timeline.html')
