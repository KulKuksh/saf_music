from django import forms
from .models import Genre
from .models import Track
from .models import Artist

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name_ru', 'name_en', 'description']
        labels = {
            'name_ru': 'Название на русском',
            'name_en': 'Название на анг',
            'description': 'Описание',
        }
class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
        labels = {
            'title': 'Название',
            'duration': 'Длительность',
            'genres': 'Жанр',
        }

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        labels = {
            'name': 'Имя/Название',
            'image': 'Фотография',
        }
    
    
    
    