from django.shortcuts import render

from gameplay.models import Game

# Create your views here.


def home(request):
    """
    games_first_player = Game.objects.filter(
        first_player=request.user,  # This is how we check if there is a
                                    # login session associated with the current request.
                                    # If there is somebody logged in, 'first_player'
                                    # will contain the 'User' instance referencing the user who
                                    # is viewing his own player page.
        status='F'
    )

    games_second_player = Game.objects.filter(
        second_player=request.user,
        status='S'
    )

    all_my_games = list(games_first_player) + list(games_second_player)
    """
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()  # Here we select all the games of the logged in user that are not finished yet.

    return render(request, 'player/home.html', {'active_games': active_games})

