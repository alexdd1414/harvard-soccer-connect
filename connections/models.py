from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # first_name = models.CharField(max_length=40, default='')
    # last_name = models.CharField(max_length = 40, default='')
    # email = models.EmailField()

    def __str__(self):
        return self.user.username
    
def create_player(sender, **kwargs):
    if kwargs['created']:
        user_profile = Player.objects.create(user=kwargs['instance'])

post_save.connect(create_player, sender=User)


# class UserProfileManager(models.Manager):
#     def get_queryset(self):
#         return super(UserProfileManager, self).get_queryset().filter(city='London')

# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     description = models.CharField(max_length=100, default='')
#     city = models.CharField(max_length=100, default='')
#     website = models.URLField(default='')
#     phone = models.IntegerField(default=0)
#     image = models.ImageField(upload_to='profile_image', blank=True)

#     # london = UserProfileManager()

#     def __str__(self):
#         return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender=User)


# FRESHMAN = 'FR'
    # SOPHOMORE = 'SO'
    # JUNIOR = 'JR'
    # SENIOR = "SR"
    # YEAR_IN_SCHOOL_CHOICES = [
    #     (FRESHMAN, 'Freshman'),
    #     (SOPHOMORE, 'Sophomore'),
    #     (JUNIOR, 'Junior'),
    #     (SENIOR, 'Senior'),
    # ]
    # POSITIONS = [
    #     ('G', 'Goalkeeper'),
    #     ('D', 'Defender'),
    #     ('M', 'Midfield'),
    # #     ('F', 'Forward'),
    # ]

    # (widget=models.EmailInput({'placeholder': 'test@example.com'}))
    # position = models.CharField(max_length=15, choices=POSITIONS)
    # year = models.CharField(max_length=15, choices=YEAR_IN_SCHOOL_CHOICES)
    # concentration = models.TextField(blank=True, null=True)
    # hometown = models.TextField(blank=True, null=True)
    # internship = models.TextField(blank=True, null=True)
    # postgrad = models.TextField(blank=True, null=True)
    # longterm = models.TextField(blank=True, null=True) 
    # linkedin = models.URLField(default='')
    # plans = models.TextField(blank=True, null=True)
    # image =models.URLField(default='')
    # points = models.IntegerField(null=True)