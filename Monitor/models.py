from django.db import models
import uuid

class MonitoredInterface(models.Model):
    external_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    mac_address = models.CharField(max_length=12)
    ipv4_address = models.CharField(max_length=200)
    interface_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class BadMacAddresses(models.Model):
    external_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    mac_address = models.CharField(max_length=200)
    ipv4_address = models.CharField(max_length=200)
    interface_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)    