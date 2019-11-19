# Create your models here.
from django.db import models
from django.utils import timezone
import os
import random

# Create your models here.

def firmware_ditrectory_path(instance, filename):
    return os.path.join("firmware", instance.manufacture, instance.deviceName, filename)

class Firmwaredata(models.Model):
    manufacture = models.CharField(db_column = 'manufacture', max_length=10)
    deviceName = models.CharField(db_column = 'deviceName', max_length=10, default="")
    firmware_version = models.IntegerField(db_column='firmware_version', default=1)
    firmware_number = models.IntegerField(db_column='firmware_number', default=1)
    file = models.FileField(upload_to=firmware_ditrectory_path, null=True, blank=True)
    update_date= models.DateTimeField(db_column='update_date', default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.manufacture, self.firmware_version)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super(Firmwaredata, self).delete(*args, **kwargs)


class Devicedata(models.Model):
    manufacture = models.CharField(db_column = 'manufacture', max_length=10)
    deviceName = models.CharField(db_column = 'deviceName', max_length=20, default="")
    deviceid = models.CharField(db_column ='diviceid', max_length=10)
    firmware_version = models.IntegerField(db_column='firmware_version', default=1)
    update_date= models.DateTimeField(db_column='update_date', default=timezone.now)

    def __str__(self):
        return '%s - %d - %s' % (self.manufacture, self.firmware_version, self.deviceid)
