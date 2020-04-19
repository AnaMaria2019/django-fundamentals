from django.conf import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:id>', game_detail, name='game_detail'),
    path('make_move/<int:id>', make_move, name='game_make_move'),
    path('all_games', AllGamesList.as_view()),  # By default this view class search for a template called 'game_list'
    # (that's the reason why we created a template with the same name, if we want to name the html differently
    # we have to pass an additional argument like this 'AllGamesList.as_view(template_name='that_name.html')' ).
]
