# Generated by Django 2.0.4 on 2018-04-21 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20180420_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchup',
            name='homeTeamID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='backend.Team'),
        ),
    ]
