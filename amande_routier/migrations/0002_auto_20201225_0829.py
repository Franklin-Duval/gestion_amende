# Generated by Django 3.1.2 on 2020-12-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amande_routier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infraction',
            name='lieux',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='infraction',
            name='payé',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='matricule_vehicule',
            name='carte_grise',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]