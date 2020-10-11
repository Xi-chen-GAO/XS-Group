from django.db import models


# Create your models here.


class Question(models.Model):
    x = models.CharField(max_length=200, null=True)
    y = models.CharField(max_length=200, null=True)
    unique_squirrel_id = models.CharField(max_length=200, null=True)
    hectare = models.CharField(max_length=200, null=True)
    shift = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=200, null=True)
    hectare_squirrel_number = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=200, null=True)
    primary_fur_color = models.CharField(max_length=200, null=True)
    highlight_fur_color = models.CharField(max_length=200, null=True)
    combination_of_primary_and_highlight_color = models.CharField(max_length=200, null=True)
    color_notes = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    above_ground_sighter_measurement = models.CharField(max_length=200, null=True)
    specific_location = models.CharField(max_length=200, null=True)
    running = models.CharField(max_length=200, null=True)
    chasing = models.CharField(max_length=200, null=True)
    climbing = models.CharField(max_length=200, null=True)
    eating = models.CharField(max_length=200, null=True)
    foraging = models.CharField(max_length=200, null=True)
    other_activities = models.CharField(max_length=200, null=True)
    kuks = models.CharField(max_length=200, null=True)
    quaas = models.CharField(max_length=200, null=True)
    moans = models.CharField(max_length=200, null=True)
    tail_flags = models.CharField(max_length=200, null=True)
    tail_twitches = models.CharField(max_length=200, null=True)
    approaches = models.CharField(max_length=200, null=True)
    indifferent = models.CharField(max_length=200, null=True)
    runs_from = models.CharField(max_length=200, null=True)
    other_interactions = models.CharField(max_length=200, null=True)
    lat_long = models.CharField(max_length=200, null=True)