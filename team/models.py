from django.db import models

# Create your models here.

class players(models.Model):
    name = models.CharField(max_length=200)
    sports = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    nationalteam = models.CharField(max_length=200)
    club = models.CharField(max_length=200)
    gameplayed = models.CharField(max_length=200)
    peviospoint = models.CharField(max_length=200, default=0)
    newpoint = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    dreamteam = models.CharField(max_length=200)
    captiancy = models.CharField(max_length=200)
    vicecaptiancy = models.CharField(max_length=200)
