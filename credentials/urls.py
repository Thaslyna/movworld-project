from django.urls import path
from . import views

app_name = 'credential'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('sign-out/', views.signout, name="sign-out"),
    path('user_det/<int:u_id>/', views.user_det, name="user_detail")
]
