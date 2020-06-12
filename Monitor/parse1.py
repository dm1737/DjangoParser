def parse1(data):
    #Input is string of data from 'https://next.json-generator.com/api/json/get/41wV8bj_O'
    #Output is 2-D list containing mac addresses, interface names, and ipv4 addresses
    #Parses the needed data from 'https://next.json-generator.com/api/json/get/41wV8bj_O'

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

