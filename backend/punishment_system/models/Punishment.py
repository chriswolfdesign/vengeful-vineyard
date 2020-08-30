class Punishment(models.Model):
    type = models.ForeignKey(PunishmentType, on_delete=models.CASCADE)
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="punishments")
    giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="punishments_given")
    group = models.ForeignKey(VineyardGroup, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.reason