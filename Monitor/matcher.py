import re

def match(mac, srch = re.compile(r'[^A-F0-9]').search):
    #Input mac address string
    #Output boolean value signifying if the mac address contains only characters A-F and 0-9
    #Determines if mac address contains only valid characters

    return not bool(srch(mac))
