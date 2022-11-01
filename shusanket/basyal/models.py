from email.policy import default
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

class Task(models.Model):
    namet = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
     