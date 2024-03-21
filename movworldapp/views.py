from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404, redirect

from reviewapp.models import Review
from .models import MovieCategory
from .models import MovieList


# Create your views here.


def home(request, c_id=None):
    c_page = None
    mov_list = None
    if c_id is not None:
        c_page = get_object_or_404(MovieCategory, id=c_id)
        mov_list = MovieList.objects.all().filter(category=c_page)
    else:
        mov_list = MovieList.objects.all()
    paginator = Paginator(mov_list, 50)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        mov = paginator.page(page)
    except(EmptyPage, InvalidPage):
        mov = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'mov_cat': c_page, 'mov': mov, 'mov_list': mov_list})


def detail(request, c_id, m_id):
    if request.user.is_authenticated:
        try:
            mov_det = MovieList.objects.get(category__id=c_id, id=m_id)
        except Exception as e:
            raise e
    else:
        return redirect('credential:signin')
    rev = Review.objects.filter(movie_id=mov_det.id)
    return render(request, 'detail.html', {'mov_det': mov_det, 'rev': rev})


