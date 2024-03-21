from django.urls import path
from . import views


app_name = 'add_'

urlpatterns = [
    path('add_movie/', views.add, name="add_mov"),
    path('update/<int:up_id>/', views.update, name="update"),
    path('delete/<int:del_id>/', views.delete, name="delete"),
]
