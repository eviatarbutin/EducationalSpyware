from scapy.sendrecv import sniff 
from scapy.packet import Packet
from scapy.plist import PacketList
from scapy.layers.l2 import Ether
from scapy.layers.dns import DNSQR

"""
Converts packet from type bytes to type Packet. 

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

"""
Converts packet from type Packet to type bytes. 

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

"""
Filter DNSQR packets

Parameters
-------------
packet : Packet
    The packet that mb has to be filtered

Returns
--------
bool
    True if the packet needs to be stored, False if the packet needs to be filtered.
"""
def lfiltr(packet:Packet) -> bool:
    return DNSQR in packet 

"""
Sniffs packets for a period of time with a filter to a certain ip

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
def packet_sniff(number_of_packets=1) -> PacketList: 
    data = sniff(count=number_of_packets)
    return data

