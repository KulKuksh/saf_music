from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Breed, Dog
def main(request):
    por = Breed.objects.all()
    dog = Dog.objects.all()
    return render(request, 'index.html', {'por': por, 'dog': dog})

def breed(request, id_breed):
    breeds = Breed.objects.all()
    dogs = Dog.objects.filter(breed_id = id_breed)
    return render(request, 'index.html', {'por': breeds, 'dog': dogs})

def dog_info(request, id_dog):
    breeds = Breed.objects.all()
    dog = Dog.objects.get(id=id_dog)
    return render (request, 'info1.html', {'por': breeds})

def breed_list(request):
    breeds = Breed.objects.all()
    return render(request, 'list.html', {'breeds': breeds})

def photos(request):
    breeds = Breed.objects.all()
    dogs = Dog.objects.all()
    return render(request, 'photos.html', {'breeds': breeds, 'dogs': dogs})

def about(request):
    breeds = Breed.objects.all()
    return render(request, 'onas.html', {'breeds': breeds})

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

def addDog(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    weight = request.POST.get("weight")
    description = request.POST.get("desc")
    breed_id = request.POST.get("breed")
    breed = Breed.objects.get(id=breed_id)
    photo = request.FILES['image']
    dog = Dog()
    dog.name = name
    dog.age = age
    dog.weight = weight
    dog.description = description
    dog.breed = breed
    dog.photo = photo
    dog.save()
    return HttpResponseRedirect("/adddogform")

def formEditBreed(request, id_breed):
    breed = Breed.objects.get(id=id_breed)
    return render(request, 'updateBreed.html', {'oldName': breed, 'id': id_breed})

def editBreed(request):
    id = request.POST.get("id")
    name = request.POST.get("title")
    breed = Breed.objects.get(id=id)
    breed.title = name
    breed.save()
    return HttpResponseRedirect("/editbreedform/"+id)

def formEditDog(request, id_dog):
    breeds = Breed.objects.all()
    dog = Dog.objects.get(id=id_dog)
    return render(request, 'updateDog.html',{'old': dog, 'id': id_dog, 'breeds': breeds})

def editDog(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    age = request.POST.get("age")
    weight = request.POST.get("weight")
    description = request.POST.get("desc")
    breed_id = request.POST.get("breed")
    breed = Breed.objects.get(id=breed_id)
    photo = None
    if 'image' in request.FILES:
        photo = request.FILES['image']
    dog = Dog.objects.get(id=id)
    dog.name = name
    dog.age = age
    dog.weight = weight
    dog.description = description
    dog.breed = breed
    if photo != None:
        dog.photo = photo
    dog.save()
    return HttpResponseRedirect("/editdogform/"+id)

def deleteBreed(request, id_breed):
    breed = Breed.objects.get(id=id_breed)
    breed.delete()
    return HttpResponse('<h1>Порода успешно удалена</h1><br><a href="/">На главную</a>')

def deleteDog(request, id_editDog):
    dog = Dog.objects.get(id=id_editDog)
    dog.delete()
    return HttpResponse('<h1>Собака успешно удалена</h1><br><a href="/">На главную</a>')

