from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    vozr = models.IntegerField()
    grupp = models.CharField(max_length=10)
    
    
    


