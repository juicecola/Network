
from django.urls import path

from . import views

from .views import ProfileView, follow_user, unfollow_user

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('<str:username>/', ProfileView.as_view(), name='profile'),
    path('<str:username>/follow/', follow_user, name='follow_user'),
    path('<str:username>/unfollow/', unfollow_user, name='unfollow_user'),
]
