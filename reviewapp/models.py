from django.db import models
from django.urls import reverse

from credentials.views import User
from movworldapp.models import MovieList


# Create your models here.

class Review(models.Model):

    comment = models.TextField(max_length=200)
    movie = models.ForeignKey(MovieList, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.movie.title)

    def get_url(self):
        return reverse('add_re:add_rev', args=[str(self.id)])




