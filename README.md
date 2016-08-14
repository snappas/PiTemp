# PiTemp
Python, Raspberry Pi, DS18B20 temperature sensor, TCP sockets, multithreading, Python Tkinter GUI

Server listens for new connections.

Client connects to the TCP server.

Server creates a new thread when a client connects and sends it the sensor data every 1 second.

Client reads the data on the socket. 

GUI uses the Client to update the text label every 1 second. 
