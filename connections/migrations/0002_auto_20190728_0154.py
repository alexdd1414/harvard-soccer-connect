# Generated by Django 2.2.3 on 2019-07-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='points',
            field=models.IntegerField(null=True),
        ),
    ]
