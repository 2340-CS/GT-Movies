#from django.db import models
#from django.contrib.auth.models import User

#class Movie(models.Model):
   # movie_name = models.CharField(max_length=100)
    #description = models.TextField()
    #duration = models.DurationField()
    #price = models.FloatField()
    #RatingType = models.TextChoices("RatingType", "G PG PG-13 R")
    #rating = models.CharField(choices=RatingType)
    #genre = models.CharField(max_length=30)

#class Review(models.Model):
   # id = models.AutoField(primary_key=True)
    #comment = models.TextField()
    #date = models.DateTimeField(auto_now_add=True)
    #movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #def __str__(self):
        #return str(self.id) + ' - ' + self.movie.name
    