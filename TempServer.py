#!/usr/bin/python2.7

from w1thermsensor import W1ThermSensor
from socket import *
from threading import *
from time import *


class Server:
    def __init__(self, (server_host, server_port)):
        try:
            self.serverSocket = socket(AF_INET, SOCK_STREAM)
            self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            self.serverSocket.bind((server_host, server_port))
            self.serverSocket.listen(5)
            self.sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0000052221a6")
        except error, (value, message):
            if self.serverSocket:
                self.serverSocket.close()
            print 'Error: %s' % message
            sys.exit(1)

    def run(self):
        print 'Listening'
        while True:
            req = Request(self.serverSocket.accept(), self.sensor)
            req.start()


class Request(Thread):
    def __init__(self, (request_socket, request_address), sensor_):
        super(Request, self).__init__()
        self.requestSocket = request_socket
        self.requestAddress = request_address
        self.sensor = sensor_

    def run(self):
        print 'Request from %s on %s\n' % (self.requestAddress, current_thread().getName())
        print 'Active threads: %d\n' % active_count()

        try:
            while True:
                self.requestSocket.send("{0:.2f}".format(self.sensor.get_temperature(W1ThermSensor.DEGREES_F)) + '\n')
                sleep(1)
        except IOError:
            self.requestSocket.close()


if __name__ == "__main__":
    s = Server(('', 30000))
    s.run()
