from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#A view funtion is a funtion that takes a request and gives the Response
#In some frameworks it is called Action

def hello_world(request):
    return HttpResponse('Hello World Welcome to Django')