from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return HttpResponse("Hello world!")


def login(request):
    return HttpResponse("Hello world!")


def logout(request):
    return HttpResponse("Hello world!")
