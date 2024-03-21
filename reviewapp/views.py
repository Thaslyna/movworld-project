from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from movworldapp.models import MovieList
from reviewapp.models import Review


def movie_det(request, m_slug):
    mv = MovieList.objects.get(m_slug=m_slug)
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment = request.POST['comment']
            rating = request.POST['rating']
            user = User.objects.get(id=request.user.id)
            Review.objects.create(comment=comment, rating=rating, user=user, movie=mv)
            return redirect('rev_rate:movie_details_fun', m_slug)
    else:
        return redirect('credential:signin')
    return render(request, 'mov_det_fun.html', {'mov': mv})
