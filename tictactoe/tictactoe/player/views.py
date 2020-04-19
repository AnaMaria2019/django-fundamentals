from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from gameplay.models import Game
from .forms import InvitationForm
from .models import Invitation

# With the '@login_required' attached only the logged in users will be able to access the 'home' view.
# If you are not logged in you are redirected to the 'LOGIN_URL' configured in 'settings.py'.


@login_required
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
    invitations = request.user.invitations_received.all()
    return render(request, 'player/home.html', {'active_games': active_games, 'invitations': invitations})


@login_required
def new_invitation(request):
    if request.method == 'POST':
        invitation = Invitation(from_user=request.user)
        # the form will take the 'Invitation' instance and add it to the data received from the request.
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InvitationForm()

    return render(request, 'player/new_invitation_form.html', {'form': form})


@login_required
def accept_invitation(request, id):
    invitation = get_object_or_404(Invitation, pk=id)

    if not request.user == invitation.to_user:
        raise PermissionDenied

    if request.method == 'POST':
        if "accept" in request.POST:
            # 'accept' is the 'name' property of one of the buttons in the 'accept_invitation_form' template.
            # This way we can check if the user accepts an invitation
            game = Game.objects.create(
                first_player=invitation.to_user,
                second_player=invitation.from_user
            )

        invitation.delete()
        return redirect('player_home')
        # Because we have a 'get_absolute_url' method in the Game class we can call the 'redirect' function
        # directly on a Game object (explanation: Django uses the 'get_absolute_url' method to get the url
        # for the game_detail page).
    else:
        return render(request, 'player/accept_invitation_form.html', {'invitation': invitation})
