from django.shortcuts import render
from .models import Portfolio
from blogapp.models import Setting

# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects

    settings = Setting.objects
   
    for a in settings.all():
        color=a.color

    return render(request, 'portfolio.html', {'portfolios': portfolios, 'color':color})