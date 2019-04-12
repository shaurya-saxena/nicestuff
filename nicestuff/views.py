from django.shortcuts import render
from django.http import HttpResponse


def redirect(request):
    return HttpResponse("You shall be redirected soon")

