import requests

from django.core.management.base import BaseCommand, CommandError

def parse1(data):

    splt1 = data.split('}')
    

    mac = []
    exp = []

    for i in splt1:
        splt2 = i.split(',')
        
        for j in splt2:
            if 'mac' in j:
                temp = j.split(':')
                mac = ''.join(temp[1:])
                mac = mac.strip('"')
            if 'interface' in j:
                temp = j.split(':')
                inter = temp[1]
                inter = inter.strip('"')
            if 'address' in j:
                temp = j.split(':')
                addr = temp[1]
                addr = addr.strip('"')
                exp.append([mac, inter, addr])
            
    return exp

def parse2(data):

    splt1 = data.split('}')


    exp = []

    for i in splt1:
        splt2 = i.split(',')
        
        for j in splt2:
            if 'mac_address' in j:
                temp = j.split(':')
                mac = temp[1]
                mac = mac.strip('"')
            if 'name' in j:
                temp = j.split(':')
                inter = temp[1]
                inter = inter.strip('"')
            if 'ipv4' in j:
                temp = j.split(':')
                addr = temp[1]
                addr = addr.strip('"')
                exp.append([mac, inter, addr])

    return exp

import re

def match(mac, srch = re.compile(r'[^A-F0-9]').search):
    return not bool(srch(mac))


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
