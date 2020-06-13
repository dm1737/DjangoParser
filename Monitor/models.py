from django.db import models
import uuid

class MonitoredInterface(models.Model):
    #Table for storing data with acceptable mac addresses
    external_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    mac_address = models.CharField(max_length=12) 
    ipv4_address = models.CharField(max_length=200) 
    interface_name = models.CharField(max_length=200) 
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        #Insure mac_address and interface_name fields are unique together
        unique_together = ('mac_address', 'interface_name')

class BadMacAddresses(models.Model):
    #Table for storing data with unacceptable mac addresses 
    #(more than 12 chars, or char values outside of A-F and 0-9)
    external_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    mac_address = models.CharField(max_length=200)
    ipv4_address = models.CharField(max_length=200)
    interface_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)    

    class Meta:
        #Insure mac_address and interface_name fields are unique together
        unique_together = ('mac_address', 'interface_name')