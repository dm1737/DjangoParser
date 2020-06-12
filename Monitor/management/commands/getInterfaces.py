import requests

from django.core.management.base import BaseCommand, CommandError

from Monitor.models import *
from Monitor.parse1 import parse1
from Monitor.parse2 import parse2
from Monitor.matcher import match

class Command(BaseCommand):
    def handle(self, *args, **options):
        url1 = 'https://next.json-generator.com/api/json/get/41wV8bj_O'
        url2 = 'https://next.json-generator.com/api/json/get/Nk48cbjdO'

        res1 = requests.get(url1)
        data1 = str(res1.content)

        res2 = requests.get(url2)
        data2 = str(res2.content)

        parsedData1 = parse1(data1)

        goodMac1 = []
        badMac1 = []

        for k in parsedData1:
            if len(k[0]) == 12:
                if match(k[0]):
                    goodMac1.append(k)
            else:
                badMac1.append(k)


        parsedData2 = parse2(data2)

        goodMac2 = []
        badMac2 = []

        for j in parsedData2:
            if len(j[0]) == 12:
                if match(j[0]):
                    goodMac2.append(j)
            else:
                badMac2.append(j)

        print(goodMac2)
