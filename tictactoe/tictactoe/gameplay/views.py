from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic.list import ListView

from .models import Game
from .forms import MoveForm


def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')  # 'player_home' is the name of the url where we want to redirect the user.
        # In this case the url is 'home' located in 'player.urls'.
    else:
        return render(request, 'tictactoe/welcome.html')


@login_required
def game_detail(request, id):
    game = get_object_or_404(Game, pk=id)
    context = {'game': game}

    if game.is_users_move(request.user):
        context['form'] = MoveForm()

    return render(request, 'gameplay/game_detail.html', context)


@login_required
def make_move(request, id):
    game = get_object_or_404(Game, pk=id)

    if not game.is_users_move(request.user):
        raise PermissionDenied

    move = game.new_move()
    form = MoveForm(instance=move, data=request.POST)

    if form.is_valid():
        move.save()
        return redirect("game_detail", id)
    else:
        return render(request, "gameplay/game_detail.html", {'game': game, 'form': form})


class AllGamesList(ListView):  # 'ListView' is a generic class view which contains methods to interact with the db.
    model = Game
