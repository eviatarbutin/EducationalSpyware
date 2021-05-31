import socket
from struct import pack

import encryption
import sniffing
from scapy.all import *

BUFFER_LENGTH = 2**15

class Server:
    def __init__(self,ip="0.0.0.0",port=8080):
        self.ip=ip
        self.port=port
        self.server_socket = socket.socket()
        self.client_socket = None
        self.client_addr = None

    def open(self):
        self.server_socket.bind((self.ip,self.port))
        self.server_socket.listen(1)
        print("Server is Up And Running")
        self.client_socket, self.client_addr = self.server_socket.accept()
        print("Client Connected")
            
    def talk(self):
        files_counter = 0

        while True: 
            print(str(files_counter) + " - waiting for packets")
            data = self.client_socket.recv(BUFFER_LENGTH)
            
            while True:
                tmp = self.client_socket.recv(BUFFER_LENGTH)
                print("recieving packets")
                data += tmp
            
                try:
                    if data[-3:].decode() == "fin":
                        data = data[:-3]
                        break
                except:
                    continue
            print(str(files_counter) + " - recieved packets")

            data = encryption.decrypt(data)
            wfile = open("packets"+str(files_counter) + ".pcap", "wb")
            wfile.write(data)
            
            wfile.close()
            
            try:
                prev_packs = rdpcap("packets.pcap")
            except:
                prev_packs:PacketList = rdpcap("packets0.pcap")
                wrpcap("packets.pcap", prev_packs)
                continue
            new_packs = rdpcap("packets"+str(files_counter) + ".pcap")
            for packet in new_packs:
                prev_packs.append(packet)    
            wrpcap("packets.pcap", prev_packs)

            files_counter += 1
            print(str(files_counter) + " - packets written")

            #data = sniffing.bytes_to_packet(data)
            #data.show()
		    
                      
def main():
    server = Server()
    server.open()
    server.talk()   

if __name__ == "__main__":
    main()
