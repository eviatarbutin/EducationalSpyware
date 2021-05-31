import socket

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
        print("Server is up and running")
        self.client_socket, self.client_addr = self.server_socket.accept()
        print("Client connected")
            
    def talk(self):
        files_counter = 0
        while True: 
            data = self.client_socket.recv(BUFFER_LENGTH)
            print(len(data))
            while True:
                tmp = self.client_socket.recv(BUFFER_LENGTH)
                data += tmp
                print(len(data))
                try:
                    print(data[-3:])
                    print(data[-3:].decode())
                    if data[-3:].decode() == "fin":
                        data = data[:-3]
                        break
                except:
                    print("nope")
                    continue
            data = encryption.decrypt(data)
            
            wfile = open("packets"+str(files_counter) + ".pcap", "wb")
            wfile.write(data)
            wfile.close()
            files_counter += 1
            print("written")
            #data = sniffing.bytes_to_packet(data)
            #data.show()
		    
                      
def main():
    server = Server()
    server.open()
    server.talk()   

if __name__ == "__main__":
    main()
