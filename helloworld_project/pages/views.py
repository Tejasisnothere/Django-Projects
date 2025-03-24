from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.f

# def homePageView(request):
#     return HttpResponse("Hello, World!")

def HomePageView(request):
    return render(request, 'home.html')

def AboutPageView(request):
    return render(request, 'about.html')
