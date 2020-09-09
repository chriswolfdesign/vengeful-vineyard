from django.db import models
from ..models import *


class VineyardGroup(models.Model):

    #TODO figure out vv group syncing
    name = models.CharField(max_length=30, unique=True)
    users = models.ManyToManyField("VineyardUser") #TODO add service to add user to group
    def __str__(self):
        return self.name