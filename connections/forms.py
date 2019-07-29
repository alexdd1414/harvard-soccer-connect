from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
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
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length = 40, required=True)
    email = forms.EmailField(required=True)
    # position = forms.MultipleChoiceField(choices=POSITIONS, widget=forms.RadioSelect(), required=True)
    # year = forms.MultipleChoiceField(choices=YEAR_IN_SCHOOL_CHOICES, widget=forms.RadioSelect(), required=True)
    # concentration = forms.CharField(widget=forms.Textarea, required=True)
    # hometown = forms.CharField(max_length=70, required=True)
    # internship = forms.CharField(widget=forms.Textarea, required=True)
    # postgrad = forms.CharField(widget=forms.Textarea, required=True)
    # longterm = forms.CharField(widget=forms.Textarea, required=True)
    # # # linkedin = forms.URLField(default='', required=True)
    # plans = forms.CharField(widget=forms.Textarea, required=True)
    # # image = forms.URLField(default='', required=True)
    # # points = forms.IntegerField()

    class Meta: 
        model = User
        fields = {
            'username', 
            'password1',
            'password2',
            'first_name', 
            'last_name',
            'email',
            # 'position',
            # 'year',
            # 'concentration',
            # 'hometown',
            # 'internship',
            # 'postgrad',
            # 'longterm',
            # # 'linkedin',
            # 'plans',
            # 'image',
            # 'points'
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email= self.cleaned_data['email']
        # user.position = self.cleaned_data['position']
        # user.year = self.cleaned_data['year']
        # user.concentration = self.cleaned_data['concentration']
        # user.hometown = self.cleaned_data['hometown']
        # user.internship = self.cleaned_data['internship']
        # user.postgrad = self.cleaned_data['postgrad']
        # user.lonterm = self.cleaned_data['longterm']
        # # user.linkedin = self.cleaned_data['linkedin']
        # user.plans = self.cleaned_data['plans']
        # # user.image = self.cleaned_data['image']
        # user.points = self.cleaned_data['points']

        if commit:
            user.save()

        return user



