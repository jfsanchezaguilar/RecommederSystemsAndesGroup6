from __future__ import unicode_literals

from django.db import models


# Create your models here.
class RecommendTask(models.Model):
    training = models.IntegerField()
    similarity = models.CharField(max_length=20)
    algorithm = models.CharField(max_length=20)
    added_date = models.DateTimeField("date added")
    start_date = models.DateTimeField("date started", null=True)
    finish_date = models.DateTimeField("date finished", null=True)
    status = models.IntegerField()
