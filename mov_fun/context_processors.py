from movworldapp.models import MovieCategory


def MovieCategories(request):
    categories = MovieCategory.objects.all()
    return dict(movie_cat=categories)
