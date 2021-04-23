from scapy.all import *
from scapy.sendrecv import sniff 

'''
seconds - number of seconds to sniff each time.
filter_ip - the ip address to filter the sniffing from, should be the server's ip.
return list - list of bytes where each element is a packet 
'''
def timed_sniff(seconds: int, filter_ip: str) -> list: 
    filter = f"not src host {filter_ip}"
    data = sniff(timeout = seconds, filter = filter)

    #The following part may get removed
    length = 0
    for p in data:
        length += len(p)
    #

    byte_list = []
    for p in data:
        byte_list.append(bytes(p))

    return byte_list
