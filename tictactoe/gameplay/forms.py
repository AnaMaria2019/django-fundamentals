from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Move


class MoveForm(ModelForm):
    class Meta:
        model = Move
        exclude = []

    """Overriding the 'clean' method enables us to do custom validation. Before this method gets called the ModelForm 
        class will validate each field and put the resulting value in a dictionary called 'self.cleaned_data'."""

    def clean(self):
        x = self.cleaned_data.get("x")  # If the validation fails the value of this field will be None.
        # If the validation succeeds the fields will contain the user's input.
        y = self.cleaned_data.get("y")
        game = self.instance.game

        try:
            if game.board()[y][x] is not None:
                raise ValidationError("Square is not empty!")
        except IndexError:
            raise ValidationError("Invalid coordinates")

        return self.cleaned_data
