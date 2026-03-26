from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Genre, Track, Artist
from .forms import GenreForm, TrackForm, ArtistForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def genres(request):
    name = Genre.objects.all()
    return render(request, 'genres.html', {'name': name})

def deletegenre(request, id_genre):
    genre = Genre.objects.get(id = id_genre)

    genre.delete()
    return HttpResponse('<h1>Жанр удален</h1><a href="/">На главную</a>')

def editgenre(request, id_genre):
    genr = Genre.objects.get(id=id_genre)
    
    if request.method == "POST":
        genre = GenreForm(request.POST, instance=genr)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    else:
        genreform = GenreForm(instance=genr)
        return render(request, "editgenre.html", {'form': genreform})
    

def add_genre(request):
    if request.method == "POST":
        genre = GenreForm(request.POST)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
        
    else:
        genreform = GenreForm()
        return render(request, "add_genre.html", {'form': genreform})
    
def track(request):
    tracks = Track.objects.all()
    
    return render(request, "track.html", {'track': track})

def addtrack(request):
    if request.method == "POST":
        track = TrackForm(request.POST)
        if track.is_valid():
            track.save()
        return redirect('/track')
        
    else:
        track = TrackForm()
        return render(request, "addtrack.html", {'form': TrackForm})
    
def deletetrack(request, id_track):
    track = Track.objects.get(id = id_track)

    track.delete()
    return HttpResponse('<h1>Трек удален</h1><a href="/track">На главную</a>')

def edittrack(request, id_track):
    trac = Track.objects.get(id = id_track)
    
    if request.method == "POST":
        track = TrackForm(request.POST, instance=trac)
        if track.is_valid():
            track.save()
        return redirect('/track')
    else:
        trackform = TrackForm(instance=trac)
        return render(request, "edittrack.html", {'form': trackform})
    
def artists(request):
    a = Artist.objects.all()
    return render(request, 'artists.html', {'artists': a})

    