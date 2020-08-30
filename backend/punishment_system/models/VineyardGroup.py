class VineyardGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    users = models.ManyToManyField(to=User)
    def __str__(self):
        return self.name