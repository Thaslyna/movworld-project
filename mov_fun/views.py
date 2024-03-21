from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views.generic import DeleteView

from mov_fun.forms import MovieForm
from movworldapp.models import MovieList, MovieCategory

from django.shortcuts import render, redirect
from movworldapp.models import MovieList


def add(request):
    if request.method == 'POST':
        movie_name = request.POST['title']
        m_slug = slugify(movie_name)
        mov_date = request.POST['date']
        mov_desc = request.POST['desc']
        mov_actrs = request.POST['actrs']
        mov_img = request.FILES['img']
        movie_cat = request.POST['category']
        category = MovieCategory.objects.get(id=movie_cat)
        mov_link = request.POST['link']
        if not request.user.is_authenticated:
            return redirect('credential:signin')
        else:
            user = User.objects.get(id=request.user.id)
            mov_add = MovieList(title=movie_name, release_date=mov_date, category=category, link=mov_link,
                                actors=mov_actrs, poster=mov_img, desc=mov_desc, added_by=user, m_slug=m_slug)
            mov_add.save()
            return redirect('/')

    return render(request, 'add.html')


def update(request, up_id):
    movie_mo = MovieList.objects.get(id=up_id)
    if movie_mo.added_by == request.user:
        movie_fo = MovieForm(request.POST or None, instance=movie_mo)
        if movie_fo.is_valid():
            movie_mo.m_slug = slugify(movie_mo.title)
            movie_fo.save()
            return redirect('/')
    else:
        messages.info(request, "You are not authorized to update this movie.")
        return render(request, 'error.html')
    return render(request, 'update.html', {'mov_mo': movie_mo, 'mov_fo': movie_fo})


def delete(request, del_id):
    movie_mo = MovieList.objects.get(id=del_id)
    if request.user == movie_mo.added_by:
        movie_mo.delete()
        return redirect('/')
    else:
        messages.info(request, 'You are not authorized to delete this movie.')
    return render(request, 'delete.html')


# def delete(request, delete_id):
#     movie_mo = MovieList.objects.get(id=delete_id)
#     if movie_mo.added_by == request.user:
#         movie_mo.delete()
#         return redirect('/')
#     else:
#         del_msg = 'You are not authorized to delete this movie.'
#     return render(request, 'delete.html', {'del': del_msg})

# def delete(request, delete_id):
#     movie = get_object_or_404(MovieList, id=delete_id)
#     if request.method == 'POST':
#         # Check if the user is the creator of the movie
#         if movie.added_by == request.user:
#             movie.delete()
#             return redirect('/')
#         else:
#             return render(request, 'error.html', {'msg': 'You are not authorized to delete this movie.'})
#     return render(request, 'delete.html', {'movie': movie})


# def delete(request, delete_id):
#     if request.method == "POST":
#         movie_del = MovieList.objects.get(id=delete_id)
#         if movie_del.added_by == request.user:
#             movie_del.delete()
#             return redirect('/')
#     else:
#         messages.info(request, "You are not able to delete this Movie.")
#         return redirect('/')
#     return render(request, 'delete.html')
