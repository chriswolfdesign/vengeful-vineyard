from django.db import models
from ..models import *

class VineyardUser(models.Model):
    #objects = UserManager()
    #leaderboard = LeaderBoardManager()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    username = models.CharField(max_length=100)

    @property
    def name(self):
        return self.first_name + " " + self.last_name
