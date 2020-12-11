from django.db import models

# Create your models here.
class Movie_Data(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=100)
    overview = models.CharField(max_length=1000)
    popularity = models.FloatField()

    def __str__(self):
        return self.title 