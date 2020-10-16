from django.db import models


# Create your models here.


class Squirrel(models.Model):
    AGE_CHOICES = (
        ("Adult", "ADULT"),
        ("Juvenile", "JUVENILE"),
        ("?", "?"),
    )

    SHIFT_CHOICES = (
        ("PM", "PM"),
        ("AM", "AM"),
    )

    LOCATION_CHOICES = (
        ("Ground Plane", "GROUND PLANE"),
        ("Above Ground", "ABOVE GROUND"),
    )

    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    unique_squirrel_id = models.CharField(max_length=200, null=True)
    hectare = models.CharField(max_length=200, null=True)
    shift = models.CharField(max_length=200, choices=SHIFT_CHOICES, null=True)
    date = models.DateField(null=True)
    hectare_squirrel_number = models.IntegerField(null=True)
    age = models.CharField(max_length=200, choices=AGE_CHOICES, null=True)
    primary_fur_color = models.CharField(max_length=200, null=True)
    highlight_fur_color = models.CharField(max_length=200, null=True)
    combination_of_primary_and_highlight_color = models.CharField(max_length=200, null=True)
    color_notes = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES, null=True)
    above_ground_sighter_measurement = models.CharField(max_length=200, null=True)
    specific_location = models.CharField(max_length=200, null=True)
    running = models.BooleanField(null=True)
    chasing = models.BooleanField(null=True)
    climbing = models.BooleanField(null=True)
    eating = models.BooleanField(null=True)
    foraging = models.BooleanField(null=True)
    other_activities = models.CharField(max_length=200, null=True)
    kuks = models.BooleanField(null=True)
    quaas = models.BooleanField(null=True)
    moans = models.BooleanField(null=True)
    tail_flags = models.BooleanField(null=True)
    tail_twitches = models.BooleanField(null=True)
    approaches = models.BooleanField(null=True)
    indifferent = models.BooleanField(null=True)
    runs_from = models.BooleanField(null=True)
    other_interactions = models.CharField(max_length=200, null=True)
    lat_long = models.CharField(max_length=200, null=True)
