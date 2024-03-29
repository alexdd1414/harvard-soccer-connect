# Generated by Django 2.2.3 on 2019-07-27 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=40)),
                ('last_name', models.CharField(default='', max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(choices=[('G', 'Goalkeeper'), ('D', 'Defender'), ('M', 'Midfield'), ('F', 'Forward')], max_length=1)),
                ('year', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], max_length=2)),
                ('concentration', models.TextField(blank=True, null=True)),
                ('hometown', models.TextField(blank=True, null=True)),
                ('internship', models.TextField(blank=True, null=True)),
                ('postgrad', models.TextField(blank=True, null=True)),
                ('longterm', models.TextField(blank=True, null=True)),
                ('linkedin', models.URLField(default='')),
                ('plans', models.TextField(blank=True, null=True)),
                ('image', models.URLField(default='')),
                ('points', models.BigIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
