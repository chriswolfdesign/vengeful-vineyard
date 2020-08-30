from django.contrib.auth.models import UserManager

class PunishmentType(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    #image = models.ImageField(upload_to="upload/")
    def __str__(self):
        return f'Name: {self.name} Value: {self.value}'
