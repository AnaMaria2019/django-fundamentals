from django.shortcuts import render, redirect

# Create your views here.


def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')  # 'player_home' is the name of the url where we want to redirect the user.
        # In this case the url is '' located in 'player.urls'.
    else:
        return render(request, 'tictactoe/welcome.html')
