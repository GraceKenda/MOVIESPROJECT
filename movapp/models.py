from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)


    def get_absolute_url(self):
        return reverse('moviesapp:index')


class Movie(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    cover = models.ImageField()
    is_new = models.BooleanField()
    url = models.URLField()
    video = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment


# Create your models here.
