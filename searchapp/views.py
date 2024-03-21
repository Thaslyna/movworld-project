from django.shortcuts import render

from django.db.models import Q

from movworldapp.models import MovieList


def search(request):
    movie = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movie = MovieList.objects.all().filter(Q(title__icontains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'query': query, 'movie': movie})
