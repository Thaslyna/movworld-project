from django.urls import path
from . import views

app_name = 'mov_wo'

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:c_id>/', views.home, name="mov_by_cat"),
    path('<int:c_id>/<int:m_id>/', views.detail, name="mov_detail"),

]
