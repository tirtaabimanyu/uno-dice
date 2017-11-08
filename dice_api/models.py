from django.db import models

class Dice(models.Model):
    mode = models.CharField(max_length=16)
    face = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
