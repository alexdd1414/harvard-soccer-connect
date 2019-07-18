import datetime

from django.db import models
from django.utils import timezone

class Player(models.Model):
    player_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    def __str__(self):
        return self.player_text
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Position(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    position_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.position_text


