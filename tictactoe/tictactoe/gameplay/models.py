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
