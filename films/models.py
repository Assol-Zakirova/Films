from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=255)
    episodes = models.IntegerField(default=0)
    genre = models.TextField()
