from socket import *


class TempClient:
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)

    def connect(self, host_, port_):
        self.sock.connect((host_, int(port_)))

    def read(self):
        response = self.sock.recv(256)
        if len(response) == 0:
            exit(1)
        else:
            return response
