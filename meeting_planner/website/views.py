from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Meeting Plannner!")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("Hi I'm Victor Del Rio and I implement ideas into robust projects!")