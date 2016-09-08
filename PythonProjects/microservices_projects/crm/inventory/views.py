from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    content = 'Welcome to Inventory Services'
    return HttpResponse(content)
