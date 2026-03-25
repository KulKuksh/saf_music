from django.db import models

class Breed(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    def __str__(self):
        return self.title

class Dog(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    weight = models.FloatField()
    description = models.TextField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name