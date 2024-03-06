from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User, Post
from .forms import NewPostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            # Create a new post instance and save it to the database
            new_post = Post(content=content, user=request.user)
            new_post.save()
            return JsonResponse({'success': True})  # Return success response
        else:
            # Return error response if form is invalid
            return JsonResponse({'success': False, 'error': 'Invalid form data'})
    else:
        form = NewPostForm()  # Create a new instance of the form
    return render(request, 'network/new_post.html', {'form': form})


def profile(request, username):
    user = get_object_or_404(User, username=username)

    # Retrieve the count of followers and following users
    followers_count = user.followers.count()
    following_count = user.following.count()

    # Retrieve all posts associated with the user in reverse chronological order
    posts = Post.objects.filter(user=user).order_by('-timestamp')

    # If the logged-in user is not the same as the displayed user, determine if the logged-in user is following the displayed user
    if request.user != user:
        is_following = user.followers.filter(
            username=request.user.username).exists()
    else:
        is_following = False

    context = {
        'user': user,
        'followers_count': followers_count,
        'following_count': following_count,
        'posts': posts,
        'is_following': is_following,
    }

    return render(request, 'profile.html', context)


@login_required
def toggle_follow(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    # Toggle follow status
    if request.user != user_to_follow:
        if request.user in user_to_follow.followers.all():
            user_to_follow.followers.remove(request.user)
        else:
            user_to_follow.followers.add(request.user)

    return redirect('profile', username=username)


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'


@login_required
def follow_user(request, user_id):
    user_to_follow = User.objects.get(pk=user_id)
    request.user.following.add(user_to_follow)
    return JsonResponse({'status': 'ok'})


@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.get(pk=user_id)
    request.user.following.remove(user_to_unfollow)
    return JsonResponse({'status': 'ok'})


@login_required
def following_posts(request):
    following_users = request.user.following.all()
    following_posts = Post.objects.filter(
        user__in=following_users).order_by('-timestamp')
    return render(request, 'network/following_posts.html', {'posts': following_posts})
