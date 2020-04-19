from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Game


def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')  # 'player_home' is the name of the url where we want to redirect the user.
        # In this case the url is '' located in 'player.urls'.
    else:
        return render(request, 'tictactoe/welcome.html')


@login_required
def game_detail(request, id):
    game = get_object_or_404(Game, pk=id)

    return render(request, 'gameplay/game_detail.html', {'game': game})
