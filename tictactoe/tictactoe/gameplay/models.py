from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GAME_STATUS_CHOICES = (
    ('F', 'First player to move'),
    ('S', 'Second player to move'),
    ('W', 'First player wins'),
    ('L', 'Second player wins'),
    ('D', 'Draw')
)


class Game(models.Model):
    # 'related_name' specifies the name of the reverse relation from the 'User' model back to the 'Game' model.
    # When accessing Game.objects.filter(second_player__username='ana') for example we will get a queryset of Game
    # objects where the second_player is the user with the username 'ana' ('second_player' and 'first_player'
    # fields point to a record in the users table, meaning that these fields are not simple values, they represent
    # different objects stored in a different table). We look up all the games where the username field of that record
    # in the users table equals 'ana' (ForeignKey means a One to Many relationship).
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.CASCADE)  # Django comes with a default User class.
    second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=models.CASCADE)  # A user can play more games.
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)
    # 'choices = GAME_STATUS_CHOICES' will generate in Django a drop-down list for the status field.

    def __str__(self):
        return f"Game nr: {self.id}, {self.first_player} vs {self.second_player}"


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)  # By adding 'blank=True' we allow the user
    # to leave the comment field empty.
    by_first_player = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)  # A game has moore moves. (that means that the Game class
    # will have by default a move_set which contains all the moves. (this move_set is called 'a related manager'
    # which works just like 'objects' manager (we can call g.move_set.all() for example where g is a Game object).
