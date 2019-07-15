from django.db import models
from django.utils import timezone
import random
# Create your models here.

class Firmwaredata(models.Model):
    manufacture = models.CharField(max_length=10)
    firmware_version = models.IntegerField(default=1)
    update_date= models.DateTimeField()

    def __str__(self):
        return '%s - %s' % (self.manufacture, self.firmware_version)


class Devicedata(models.Model):
    manufacture = models.CharField(max_length=10)
    firmware_version = models.IntegerField(default=1)
    deviceid = models.CharField(max_length=10)
    update_date=models.DateTimeField()

    def __str__(self):
        return '%s - %d - %s' % (self.manufacture, self.firmware_version, self.deviceid)
