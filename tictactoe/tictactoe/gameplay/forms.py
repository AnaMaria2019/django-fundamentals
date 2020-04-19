from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Move


class MoveForm(ModelForm):
    class Meta:
        model = Move
        exclude = []

