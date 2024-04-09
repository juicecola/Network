
from django.urls import path

from . import views

from .views import ProfileView, follow_user, unfollow_user, following_posts

urlpatterns = [
    path("", views.index, name="index"),
    path('new_post/', views.new_post, name='new_post'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<str:username>/follow/', follow_user, name='follow_user'),
    path('<str:username>/unfollow/', unfollow_user, name='unfollow_user'),
    path("following/", following_posts, name="following_posts"),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('unlike/<int:post_id>/', views.unlike_post, name='unlike_post')
]
