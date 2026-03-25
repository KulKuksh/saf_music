from django.db import models

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(max_length=1000, unique=True, primary_key=True)
    name_en=models.CharField(max_length=1000, unique=True)
    name_ru=models.CharField(max_length=1000, unique=True)
    description=models.TextField()
    def __str__(self):
        return self.name_ru

class Track(models.Model):
    title = models.CharField(max_length=500, unique=True)
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    def __str__(self):
        return self.title
    