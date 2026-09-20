from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello rebel please complete the project")

def house(request):
    return HttpResponse("hello baby how are you")