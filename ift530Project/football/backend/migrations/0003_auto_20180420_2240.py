# Generated by Django 2.0.4 on 2018-04-21 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_matchup_player_roster_score_stadium_stats'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stats',
            new_name='Stat',
        ),
        migrations.AddField(
            model_name='matchup',
            name='stadiumID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.Stadium'),
        ),
    ]
