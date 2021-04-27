import socket

import encryption
import sniffing

class Client:
    def __init__(self,ip="127.0.0.1",port=8820):
        self.client_socket=socket.socket()
        self.ip = ip
        self.port = port

    def connect(self):
        self.client_socket.connect((self.ip,self.port))

    def talk(self):
        while True:
            input("Press enter to continue: ")
            
            packets = sniffing.timed_sniff(1, "1.1.1.1")
            p = packets[0]
            p = sniffing.packet_to_bytes(p)

            print(f"original: {p}")
            print("\r\n\r\n\r\n")

            p = encryption.encrypt(p)
            print(f"encrypted: {p}")

            self.client_socket.send(p)

def main():
    client = Client()
    client.connect()
    client.talk()

if __name__ == "__main__":
    main()
