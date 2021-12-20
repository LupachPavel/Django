from django.shortcuts import render
from django.http import HttpResponse
from . models import Post


def home(request):
    return render( request, 'my_project/home.html')

def about(request):
    return render( request, 'my_project/about.html')