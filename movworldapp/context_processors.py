from .models import MovieCategory


def mov_cat(request):
    links = MovieCategory.objects.all()
    return dict(links=links)
