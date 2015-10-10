from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=20, decimal_places=0)