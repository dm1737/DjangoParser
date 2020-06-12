def parse2(data):
    #Input is string of data from 'https://next.json-generator.com/api/json/get/Nk48cbjdO'
    #Output is 2-D list containing mac addresses, interface names, and ipv4 addresses
    #Parses the needed data from 'https://next.json-generator.com/api/json/get/Nk48cbjdO'
    
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

