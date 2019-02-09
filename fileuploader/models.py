from django.db import models

class Req(models.Model):
    image = models.ImageField()
    share = models.BooleanField(default=False);
    session = models.CharField(max_length=200, default='');
