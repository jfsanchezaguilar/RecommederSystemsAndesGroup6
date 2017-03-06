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


class BookUser(models.Model):
    user_id = models.IntegerField()
    location = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)


class Book(models.Model):
    isbn = models.CharField(max_length=200)
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    year_publish = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    image_small = models.CharField(max_length=2000)
    image_medium = models.CharField(max_length=2000)
    image_large = models.CharField(max_length=2000)


class BookRaiting(models.Model):
    user_id = models.IntegerField()
    isbn = models.CharField(max_length=200)
    raiting = models.IntegerField()
