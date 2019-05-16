from django.shortcuts import render
from django.http import HttpResponse
from .models import Recommendations
from .models import TxnHistory
from .models import Products
from django.contrib.auth.decorators import login_required



@login_required()
def home(request):
    rec_list = Recommendations.objects.filter(user=request.user)[:10]
    context = {'rec_list': rec_list}
    return render(request, 'home.html', context)

def history(request):
    return HttpResponse("You shall be redirected soon")

def favorites(request):
    return HttpResponse("You shall be redirected soon")