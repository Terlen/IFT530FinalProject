# Generated by Django 2.0.4 on 2018-04-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_matchup_awayteamid'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='score',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
