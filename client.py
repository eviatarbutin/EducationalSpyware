import socket
import time
import encryption
import sniffing

class Client:
    def __init__(self,ip="127.0.0.1",port=8820):
        self.client_socket=socket.socket()
        self.ip = ip
        self.port = port

    def connect(self):
        return self.client_socket.connect_ex((self.ip,self.port))

    def talk(self):
        packets = sniffing.timed_sniff(3, "1.1.1.1")
        while True:
            time.sleep(3)
            
            packets = sniffing.timed_sniff(1, "1.1.1.1")
            p = packets[0]
            p = sniffing.packet_to_bytes(p)

            p = encryption.encrypt(p)
            
            self.client_socket.send(p)
            
def main():
    client = Client()
    while client.connect() != 0:
        time.sleep(5)
    client.connect()
    client.talk()

if __name__ == "__main__":
    main()
