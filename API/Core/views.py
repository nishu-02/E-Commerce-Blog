from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Core/index.html')

def contact(request):
    return HttpResponse("This is contact page")

def about(request):
    return HttpResponse("This is about page")

def tracker(request):
    return HttpResponse("This is tracking page")

def productView(request):
    return HttpResponse("This is product view page")

def checkout(request):
    return HttpResponse("This is checkout page")

def search(request):
    return HttpResponse("This is the search page")