from django.db import models
from django.conf import settings
import random
# Create your models here.

User = settings.AUTH_USER_MODEL

tag = ["rook", "queen", "pawn", "king", "bishop", "knight"]

class Todos(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    task = models.CharField(max_length=300)
    content = models.CharField(max_length=300, blank=True, null=True)
    completion = models.BooleanField()

    def get_tag(self):
        return [random.choice(tag),random.choice(tag),random.choice(tag)]