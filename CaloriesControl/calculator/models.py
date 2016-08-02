from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unity = models.CharField(max_length=20)
    calories_per_unity = models.IntegerField()


