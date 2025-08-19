from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, CI/CD!\nThis is a simple Django application demonstrating CI/CD deployment.\nit's running successfully on your server!\ni can do this")