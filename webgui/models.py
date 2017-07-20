from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Skill(models.Model):
    # id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=50, null=True)
    technologies = models.TextField(null=True)

class Tag(models.Model):
    # EXTENSION_CHOICES = (
    #     (True,'png'),
    #     (False,'jpg')
    # )
    img = models.CharField(max_length=30, null=True)
    extension = models.CharField(max_length=4, null=True)

class Modal(models.Model):
    title = models.CharField(max_length=15, null=True)
    text = models.TextField(null=True)
    keywords = models.TextField(null=True)

class Formation(models.Model):
    # id = models.IntegerField(primary_key=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    company = models.CharField(max_length=40, null=True)
    name = models.CharField(max_length=100, null=True)
    validity = models.BooleanField(default=True)
    modal = models.OneToOneField(Modal, null=True)

class Experience(models.Model):
    # id = models.IntegerField(primary_key=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    company = models.CharField(max_length=50, null=True)
    context = models.CharField(max_length=100, null=True)
    modal = models.OneToOneField(Modal, null=True)

class Leisure(models.Model):
    label = models.CharField(max_length=25, null=True)
    description = models.TextField(null=True)
