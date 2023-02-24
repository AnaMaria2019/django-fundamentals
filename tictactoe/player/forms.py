from django.forms import ModelForm
from .models import Invitation

# The Django's 'ModelForm' class creates a Html form based on a model.


class InvitationForm(ModelForm):
    class Meta:  # The 'Meta' class's role is to configure the 'InvitationForm' class's behaviour.
        model = Invitation  # This is where we specify the model we want to generate a form for.
        exclude = ('from_user', 'timestamp')