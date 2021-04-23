from scapy.sendrecv import sniff 
from scapy.packet import Packet
from scapy.plist import PacketList

"""Converts packet from type bytes to type Packet. 

Parameters
----------
packet : bytes
    The bytes packet to convert

Returns
-------
Packet
    The packet in type Packet
"""
def bytes_to_packet(packet: bytes) -> Packet:
    return Ether(packet)

"""Converts packet from type Packet to type bytes. 

Parameters
----------
packet : Packet
    The Packet packet to convert

Returns
-------
bytes
    The packet in type bytes
"""
def packet_to_bytes(packet: Packet) -> bytes:
    return bytes(packet)

"""Sniffs packets for a period of time with a filter to a certain ip

Parameters
----------
seconds : int
    The number of seconds to sniff each time.
filter_ip : str
    The ip address to filter the sniffing from, should be the server's ip

Returns
-------
PacketList
    The list of all sniffed packets 
"""
def timed_sniff(seconds: int, filter_ip: str) -> PacketList: 
    filter = f"not src host {filter_ip}"
    data = sniff(timeout = seconds, filter = filter)

    #The following part may get removed
    length = 0
    for p in data:
        length += len(p)

    return data

