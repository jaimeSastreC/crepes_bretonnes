from django.db import models

# Create your models here.


class Crepe(models.Model):
    crepe_nom = models.CharField(unique=True, max_length=150)
    crepe_prix = models.IntegerField(blank=True, null=True)