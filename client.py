import socket

import encryption
import sniff

class Client:
    def __init__(self,ip="127.0.0.1",port=8820):
        self.client_socket=socket.socket()

    def connect(self):
        self.client_socket.connect((ip,port))

    def talk(self):
        while True:
            msg = input("Enter your input here: ")
            msg = encryption.encrypt(msg)
            print(f"the encrypted message is: {msg}")

            self.client_socket.send(msg)

     def main():
    client = Client()
    client.send_message()
