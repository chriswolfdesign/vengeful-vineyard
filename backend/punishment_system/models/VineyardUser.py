from django.contrib.auth.models import AbstractUser

class VineyardUser(AbstractUser):
    objects = UserManager()
    leaderboard = LeaderBoardManager()
    @property
    def name(self):
        return self.first_name + " " + self.last_name

User = get_user_model()