from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    allProds = []
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([products, range(1, nSlides), nSlides])
    return render(request, 'Core/index.html', {'allProds': allProds})

def contact(request):
    return HttpResponse("This is contact page")

def about(request):
    return render(request, 'Core/about.html')

def tracker(request):
    return HttpResponse("This is tracking page")

def productView(request):
    return HttpResponse("This is product view page")

def checkout(request):
    return HttpResponse("This is checkout page")

def search(request):
    return HttpResponse("This is the search page")