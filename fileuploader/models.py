from django.db import models

class Req(models.Model):
    image = models.ImageField()
    share = models.BooleanField(default=False);
