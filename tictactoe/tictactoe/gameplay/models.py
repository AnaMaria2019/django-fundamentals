from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

GAME_STATUS_CHOICES = (
    ('F', 'First player to move'),
    ('S', 'Second player to move'),
    ('W', 'First player wins'),
    ('L', 'Second player wins'),
    ('D', 'Draw')
)

BOARD_SIZE = 3

# A QuerySet represents a collection of objects from the database.
# We create our own QuerySet which will also be able to call functions like 'filter', 'exclude' etc on it.


class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):
        return self.filter(
            Q(first_player=user) | Q(second_player=user)
            # This returns all the games where the logged in user is either the first player, or the second player.
        )

    def active(self):
        return self.filter(
            Q(status='F') | Q(status='S')
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

    objects = GamesQuerySet.as_manager()
    # This will return a Manager object that includes the functions from our custom QuerySet.
    # We assign the manager to the 'objects' attribute of our Game class.
    # This means that we are overriding the 'objects' attribute, which usually holds the default manager for our model.
    # Now when we use Game.objects we have this option, for example: Game.objects.active()

    def get_absolute_url(self):
        return reverse('game_detail', args=[self.id])
        # This way we can return an url, by passing to the 'reverse' function the template name
        # and which arguments the url takes. The 'reverse' function constructs an url mapping for the
        # template given. When we retrieve a Game object from the database we can get its url too by calling
        # 'get_absolute_url' method. This method is used automatically in a 'redirect' function.
        # (See example in 'player/views' in the home view)

    def board(self):
        """Return a 2-dimensional list of Move objects, so you can ask for a state of square at position [y][x]."""
        board = [[None for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

        for move in self.move_set.all():
            board[move.y][move.x] = move

        return board

    def is_users_move(self, user):
        return (user == self.first_player and self.status == 'F') or (user == self.second_player and self.status == 'S')

    def new_move(self):
        """Returns a new move object with player, game and count preset."""

        if self.status not in 'FS':
            raise ValueError("Cannot make move on finished game!")

        return Move(
            game=self,
            by_first_player=self.status == 'F'
        )

    def update_after_move(self, move):
        """Update the status of the game, given the last move."""
        self.status = self._get_game_status_after_move(move)

    def _get_game_status_after_move(self, move):
        x, y = move.x, move.y
        board = self.board()

        if (board[y][0] == board[y][1] == board[y][2]) or \
                (board[0][x] == board[1][x] == board[2][x]) or \
                (board[0][0] == board[1][1] == board[2][2] is not None) or \
                (board[0][2] == board[1][1] == board[2][0] is not None):
            return "W" if move.by_first_player else "L"

        if self.move_set.count() >= BOARD_SIZE ** 2:
            return 'D'

        return 'S' if self.status == 'F' else 'F'

    def __str__(self):
        return f"Game nr: {self.id}, {self.first_player} vs {self.second_player}"


class Move(models.Model):
    x = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(BOARD_SIZE - 1)]
    )
    y = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(BOARD_SIZE - 1)]
    )
    comment = models.CharField(max_length=300, blank=True)  # By adding 'blank=True' we allow the user
    # to leave the comment field empty.
    by_first_player = models.BooleanField(editable=False)
    # By adding 'editable=False' we say Django that we don't want this field to show up in a form
    # (it has the same effect as if we put this field in the 'exclude' list in the MoveForm class).

    game = models.ForeignKey(Game, editable=False, on_delete=models.CASCADE)  # A game has moore moves. (that means that the Game class
    # will have by default a move_set which contains all the moves. (this move_set is called 'a related manager'
    # which works just like 'objects' manager (we can call g.move_set.all() for example where g is a Game object).

    def __eq__(self, other):
        if other is None:
            return False
        return other.by_first_player == self.by_first_player

    def save(self, *args, **kwargs):
        super(Move, self).save(*args, **kwargs)
        self.game.update_after_move(self)
        self.game.save()
