from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def harshadvalli(request):
    return HttpResponse('<h1>best python trainer</h1>')

def rakesh(request):
    return HttpResponse('<marquee><h1>best junior python trainer</h1></marquee>')