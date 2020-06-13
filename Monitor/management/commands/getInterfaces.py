import requests

from django.core.management.base import BaseCommand, CommandError

from Monitor.models import *
from django.db.models.query import QuerySet
from Monitor.parse1 import parse1
from Monitor.parse2 import parse2
from Monitor.matcher import match

class Command(BaseCommand):
    #This command is called using python manage.py getInterfaces
    #This command pulls data from two HTTP endpoints, parses the data, validates mac addresses, and stores
    #the data for the mac address, interface name, and ip address, as well as the time created, the time updated, and a unique ID
    #in an sqlite database, with the mac address and interface name being unique together
    def handle(self, *args, **options):
        #HTTP endpoints to pull data from
        BASE_URL_ALPHA = 'https://next.json-generator.com/api/json/get/41wV8bj_O'
        BASE_URL_BRAVO = 'https://next.json-generator.com/api/json/get/Nk48cbjdO'

        #pull data from alpha url and force to string
        res1 = requests.get(BASE_URL_ALPHA)
        data1 = str(res1.content)

        #pull data from bravo url and force to string
        res2 = requests.get(BASE_URL_BRAVO)
        data2 = str(res2.content)

        #Parse and clean data from alpha url
        parsedData1 = parse1(data1)

        #confirm validity of mac address and store data
        print('Processing data from alpha endpoint')
        for k in parsedData1:
            #insure length of mac address is 12 chars
            if len(k[0]) == 12:
                #insure mac address only contains chars A-F and 0-9
                if match(k[0]):
                    #If mac address and interface name are unique together, create a new entry in the 
                    #MonitoredInterface table of the database otherwise update current entry
                    monInter1 = MonitoredInterface.objects.update_or_create(mac_address=k[0], interface_name=k[1], defaults={'mac_address': k[0], 'interface_name': k[1], 'ipv4_address': k[2]})
          
            else:
                #If mac address and interface name are unique together, create a new entry in the 
                #BadMacAddresses table of the database otherwise update current entry
                badMon1 = BadMacAddresses.objects.update_or_create(mac_address=k[0], interface_name=k[1], defaults={'mac_address': k[0], 'interface_name': k[1], 'ipv4_address': k[2]})
        
        print('Data from alpha endpoint processed')

        #Parse and clean data from bravo url
        parsedData2 = parse2(data2)

        print('Processing data from bravo endpoint')
        #confirm validity of mac address and store data
        for j in parsedData2:
            #insure length of mac address is 12 chars
            if len(j[0]) == 12:
                if match(j[0]):
                    #If mac address and interface name are unique together, create a new entry in the 
                    #MonitoredInterface table of the database otherwise update current entry
                    monInter2 = MonitoredInterface.objects.update_or_create(mac_address=j[0], interface_name=j[1], defaults={'mac_address': j[0], 'interface_name': j[1], 'ipv4_address': j[2]})
                  
            else:
                #If mac address and interface name are unique together, create a new entry in the 
                #BadMacAddresses table of the database otherwise update current entry
                badMon1 = BadMacAddresses.objects.update_or_create(mac_address=j[0], interface_name=j[1], defaults={'mac_address': j[0], 'interface_name': j[1], 'ipv4_address': j[2]})
        
        print('Data from bravo endpoint processed')

       
