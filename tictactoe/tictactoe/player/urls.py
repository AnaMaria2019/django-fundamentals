from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
# 'LoginView' and 'LogoutView' are classes built in Django which provide default implementation for
# the behaviour of the login and logout pages (they are called class-based views).
from .views import *

urlpatterns = [
    path('home', home, name='player_home'),
    path('login', LoginView.as_view(template_name='player/login_form.html'), name='player_login'),
    path('logout', LogoutView.as_view(), name='player_logout'),
]

# Because 'LogoutView' is a class and not a function we need to call 'as_view' to convert it to a function.
# This has to be done when we use class-based views. To use it in the url config we call 'as_view' which
# returns a view method that can be now used in the url mapping.
# The above explanations are available for the 'LoginView' as well.
# The 'template_name' tells the LoginView class to use a specific template file to display the login form
# (the 'LoginView' class doesn't come with its own template and that's why we need to tell it where to look
# for a template).
