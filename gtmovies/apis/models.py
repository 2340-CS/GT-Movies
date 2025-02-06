from django.db import models

# Class for storing the movie model
class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    price = models.FloatField()
    RatingType = models.TextChoices("G", "PG13", "R")
    genre = models.CharField(max_length=30)



