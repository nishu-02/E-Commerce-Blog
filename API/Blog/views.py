from django.shortcuts import render
from django.http import HttpResponse

# create your views here.

def index(request):
    return render(request, 'Blog/index.html')
