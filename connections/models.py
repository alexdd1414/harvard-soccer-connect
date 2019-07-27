import datetime

from django.db import models
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
    position = models.CharField(max_length=1, choices=POSITIONS)
    year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
    concentration = models.TextField(blank=True, null=True)
    hometown = models.TextField(blank=True, null=True)
    internship = models.TextField(blank=True, null=True)
    postgrad = models.TextField(blank=True, null=True)
    longterm = models.TextField(blank=True, null=True) 
    linkedin = models.URLField(default='')
    plans = models.TextField(blank=True, null=True)
    image =models.URLField(default='')
    points = models.BigIntegerField(default=0)

# class Interests(models.Model):
#     player = models.ForeignKey(Player, on_delete=models.CASCADE)
#     interests_text = models.TextField(blank=True, null=True)