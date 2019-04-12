from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, this is the recommender web app")

def home(request):
    return HttpResponse("This is the homepage")

def redirect(request):
    return HttpResponse("You shall be redirected soon")