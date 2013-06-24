from django.db import models
from bottles.models import Bottle
from django.contrib.auth.models import User

class Party(models.Model):
    host = models.CharField(max_length=100)
    host_user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    guests = models.ManyToManyField(User, related_name='guests')
    bar_list = models.ManyToManyField(Bottle, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Parties"
