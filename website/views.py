from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>Home Page</h1>')

def about_view(request):
    return HttpResponse('<h1>About Me</h1>')

def contact_view(request):
    return HttpResponse('<h1>Contact Me</h1>')

