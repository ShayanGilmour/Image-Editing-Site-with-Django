from django.db import models
from django.utils import timezone

class Req(models.Model):
    image = models.ImageField()
    share = models.BooleanField(default=False);
    pubDate = models.DateTimeField('date published', null=True)
