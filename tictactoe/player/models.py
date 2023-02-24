from django.db import models
from django.contrib.auth.models import User


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent", on_delete=models.CASCADE)
    # 'invitations_sent' will be the name of the field inside the User class which will contain all the
    # invitations that the current user sent.
    to_user = models.ForeignKey(User, related_name="invitations_received", verbose_name="User to invite",
                                help_text="Please select the user you want to play a game with", on_delete=models.CASCADE)
    # 'verbose_name' represents the label of the field in the web page and 'help_text' provides an extra description.
    message = models.CharField(max_length=300, blank=True, verbose_name="Optional Message",
                               help_text="It's always nice to add friendly message!")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user}, {self.to_user}, {self.message}"
