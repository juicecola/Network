Network - Twitter-like Social Network
Welcome to the Network project! This project involves designing and implementing a Twitter-like social network website where users can make posts, follow other users, and interact with posts through likes. Before you begin, make sure you have watched Lecture 7 to familiarize yourself with the necessary concepts.

Getting Started
Download the distribution code from network.zip and unzip it.
In your terminal, navigate to the project4 directory.
Run python manage.py makemigrations network to create migrations for the network app.
Run python manage.py migrate to apply migrations to your database.
Understanding
The project structure includes a Django project named project4 with a single app called network. Explore the URLs, views, templates, and models provided in the distribution code.

network/urls.py: Defines the URL configuration for the app.
network/views.py: Contains views for handling routes, including user authentication, registration, and more.
network/templates/network/layout.html: Defines the HTML layout of the application.
network/models.py: Where you define models for users and other data entities.
Implementation
Your goal is to complete the implementation using Python, JavaScript, HTML, and CSS. Ensure the following requirements are met:

New Post: Allow signed-in users to create new text-based posts. This can be implemented as a separate page or a "New Post" box on the "All Posts" page.

All Posts: The "All Posts" link should display all posts from all users, showing the username, post content, timestamp, and like count. Posts should be sorted with the most recent ones first.

Profile Page: Clicking on a username should load the user's profile page, displaying follower/following counts and posts in reverse chronological order. Provide a "Follow" or "Unfollow" button for other users.

Following: The "Following" link should display posts from users the current user follows, similar to the "All Posts" page.

Pagination: Display posts 10 per page and include "Next" and "Previous" buttons for navigation.

Edit Post: Users should edit their posts by clicking an "Edit" button, allowing them to modify the content without a full page reload.

Like and Unlike: Implement a like/unlike feature that updates asynchronously using JavaScript without reloading the entire page.

Hints
Refer to Project 3 for examples of JavaScript fetch calls.
Define models in network/models.py to store necessary data.
Use Django's Paginator class for backend pagination.
Utilize Bootstrap's Pagination features for frontend display.
