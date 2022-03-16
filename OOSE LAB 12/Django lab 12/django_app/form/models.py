from django.db import models

# Create your models here.
class Player(models.Model):
    Name = models.CharField(max_length = 50)
    team = models.CharField(max_length = 50)

    def __str__(self):
        return self.Name

class Score(models.Model):
    played = models.ForeignKey(Player, on_delete=models.CASCADE)
    target = models.IntegerField()

    def __str__(self):
        return self.target