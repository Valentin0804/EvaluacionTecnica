from django.db import models

class Shelf(models.Model): # Clase Estanteria
    location = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.location

class Book(models.Model): # Clase Libro
    ISBN = models.BigIntegerField()
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    price = models.FloatField()
    shelf = models.ForeignKey(Shelf, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
