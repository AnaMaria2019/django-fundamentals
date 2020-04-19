from django.conf import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:id>', game_detail, name='game_detail'),
    path('make_move/<int:id>', make_move, name='game_make_move'),
]
