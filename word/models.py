from django.db import models
from uuid import uuid4

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=5)
    word_ac = models.CharField(max_length=5)

    # word = models.CharField(max_length=5)
    # valid_word = models.BooleanField(default=False)
    # valid_letters = models.JSONField(default=dict)
    # word_ac = models.CharField(max_length=5)


    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # word = models.CharField(max_length=5)
    # word_ac = models.CharField(max_length=5)
    # qtd_ut = models.IntegerField()
    # last_ult = models.DateField()