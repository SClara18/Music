from django.db import models

# Create your models here.

class Songs(models.Model):
    tittle = models.CharField(max_length=100000)
    artist = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    genre =models.CharField(max_length=100)
    def __str__(self):
        return self.tittle
        return self.artists
        return self.year
        return self.genre