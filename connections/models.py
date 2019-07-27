import datetime

from django.db import models
from django.utils import timezone

class Year(models.Model):
    

    year_in_school = models.CharField(
        max_length=2, 
        choices = YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

class Player(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = "SR"
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length = 40, primary_key=True)
    email = models.EmailField().db_index = True
    year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICESs)
    


    pub_date = models.DateTimeField('data published')
    def __str__(self):
        return self.player_text


class Position(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    position_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.position_text


