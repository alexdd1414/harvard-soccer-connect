import datetime

from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    POSITIONS = [
        ('G', 'Goalkeeper'),
        ('D', 'Defender'),
        ('M', 'Midfield'),
        ('F', 'Forward'),
    ]
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length = 40, default='')
    email = models.EmailField()
    # (widget=models.EmailInput({'placeholder': 'test@example.com'}))
    position = models.CharField(max_length=15, choices=POSITIONS)
    year = models.CharField(max_length=15, choices=YEAR_IN_SCHOOL_CHOICES)
    concentration = models.TextField(blank=True, null=True)
    hometown = models.TextField(blank=True, null=True)
    internship = models.TextField(blank=True, null=True)
    postgrad = models.TextField(blank=True, null=True)
    longterm = models.TextField(blank=True, null=True) 
    linkedin = models.URLField(default='')
    plans = models.TextField(blank=True, null=True)
    image =models.URLField(default='')
    points = models.IntegerField(null=True)

def create_player(sender, **kwargs):
    if kwargs['created']:
        user_profile = Player.objects.create(user=kwargs['instance'])

post_save.connect(create_player, sender=User)

# class Interests(models.Model):
#     player = models.ForeignKey(Player, on_delete=models.CASCADE)
#     interests_text = models.TextField(blank=True, null=True)