import socket

import encryption
import sniffing
from scapy.all import *

class Server:
    def __init__(self,ip="0.0.0.0",port=8820):
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
        while True: 
            data = self.client_socket.recv(4096)
            data = encryption.decrypt(data)
            
            data = sniffing.bytes_to_packet(data)
            data.show()
		    
                      
def main():
    server = Server()
    server.open()
    server.talk()   

if __name__ == "__main__":
    main()
