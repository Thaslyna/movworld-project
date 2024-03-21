
from django.urls import path
from . import views

app_name = 'rev_rate'

urlpatterns = [
    path('movie/<slug:m_slug>/', views.movie_det, name="movie_details_fun"),
]







