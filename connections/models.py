import datetime

from django.db import models
from django.utils import timezone

# class Player(forms.From):
#     FRESHMAN = 'FR'
#     SOPHOMORE = 'SO'
#     JUNIOR = 'JR'
#     SENIOR = "SR"
#     YEAR_IN_SCHOOL_CHOICES = [
#         (FRESHMAN, 'Freshman'),
#         (SOPHOMORE, 'Sophomore'),
#         (JUNIOR, 'Junior'),
#         (SENIOR, 'Senior'),
#     ]

#     POSITIONS = [
#         ('G', 'Goalkeeper'),
#         ('D', 'Defender'),
#         ('M', 'Midfield'),
#         ('F', 'Forward'),
#     ]

#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length = 40)
#     email = models.EmailField(widget=models.EmailInput({'placeholder': 'test@example.com'}, primary_key=True))
#     position = models.CharField(max_length=1, choices=POSITIONS)
#     year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
#     concentration = models.TextField(blank=True, null=True)
#     hometown = models.TextField(blank=True, null=True)
#     internship = models.TextField(blank=True, null=True)
#     postgrad = models.TextField(blank=True, null=True)
#     longterm = models.TextField(blank=True, null=True) 
#     linkedin = models.CharField(max_length=40)
#     plans = models.TextField(blank=True, null=True)
#     image = models.TextField(blank=True, null=True)
#     points = models.BigIntegerField(default=0)


# class Interests(models.Model):
#     player = models.ForeignKey(Player, on_delete=models.CASCADE)
#     interests_text = models.TextField(blank=True, null=True)