from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',)

def images(request):
    return render(request, 'images.html',)

def videos(request):
    return render(request, 'videos.html',)

def stories(request):
    return render(request, 'stories.html',)

def gifs(request):
    return render(request, 'gifs.html',)

def explore(request):
    return render(request, 'explore.html',)
