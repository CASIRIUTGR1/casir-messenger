from django.db import models
from friends.models import Friendship, FriendshipManager, FriendshipRequest

class message(models.Model):
    Auteur = models.ForeignKey('Friend')

 