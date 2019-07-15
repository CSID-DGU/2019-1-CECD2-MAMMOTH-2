from django.contrib import admin
from securefota.models import Firmwaredata
from securefota.models import Devicedata
# Register your models here.

admin.site.register(Firmwaredata)
admin.site.register(Devicedata)
