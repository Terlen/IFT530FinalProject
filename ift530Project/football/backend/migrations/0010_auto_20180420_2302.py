# Generated by Django 2.0.4 on 2018-04-21 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20180420_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='roster',
            name='beginDate',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='roster',
            name='endDate',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='roster',
            name='number',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='roster',
            name='playerID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.Player'),
        ),
        migrations.AddField(
            model_name='roster',
            name='position',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='roster',
            name='teamID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='roster',
            unique_together={('beginDate', 'playerID')},
        ),
    ]