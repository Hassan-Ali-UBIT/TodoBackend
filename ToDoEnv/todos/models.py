from django.db import models

# Create your models here.

class Todos(models.Model):
    task = models.CharField(max_length=300)
    content = models.CharField(max_length=300, blank=True, null=True)
    completion = models.BooleanField()