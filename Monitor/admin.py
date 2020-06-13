from django.contrib import admin
from .models import *

#for viewing database tables through admin page
admin.site.register(MonitoredInterface)
admin.site.register(BadMacAddresses)
