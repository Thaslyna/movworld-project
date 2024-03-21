from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from credentials.views import User


# Create your models here.

class MovieCategory(models.Model):
    category = models.CharField(max_length=200, unique=True)
    c_slug = models.SlugField(max_length=200, unique=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='cat-img')

    class Meta:
        ordering = ['category', ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('mov_wo:mov_by_cat', args=[str(self.id)])

    def __str__(self):
        return '{}'.format(self.category)


class MovieList(models.Model):
    title = models.CharField(max_length=200, unique=True)
    m_slug = models.SlugField(max_length=200, unique=True)
    poster = models.ImageField(upload_to='movie-poster')
    desc = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=500)
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE)
    link = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title', ]
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def get_url(self):
        return reverse('mov_wo:mov_detail', args=[str(self.category.id), str(self.id)])

    def __str__(self):
        return '{}'.format(self.title)



