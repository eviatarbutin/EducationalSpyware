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
            msg = input("Enter your input here: ")
            msg = msg.encode()
            msg = encryption.encrypt(msg)
            print(f"the encrypted message is: {msg}")

            self.client_socket.send(msg)

def main():
    client = Client()
    client.connect()
    client.talk()

if __name__ == "__main__":
    main()
