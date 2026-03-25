from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Breed, Dog


def index(request): 
    return render(request, 'index.html')

def formAddBreed(request):
    breeds = Breed.objects.all()
    return render(request, 'addBreed.html', {'breeds': breeds})

def addBreed(request):
    name =request.POST.get("title")
    newBreed = Breed()
    newBreed.title = name
    newBreed.save()
    return HttpResponseRedirect("/addbreedform")

def formAddDog(request):
    breeds = Breed.objects.all()
    return render(request, 'addDog.html', {'breeds': breeds})