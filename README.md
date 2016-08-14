# PiTemp
Python, Raspberry Pi, DS18B20 temperature sensor, TCP sockets, multithreading, Python Tkinter GUI

Server listens for new connections.

Client connects to the TCP server.

Server creates a new thread when a client connects and sends it the sensor data every 1 second.

Client reads the data on the socket. 

GUI uses the Client to update the text label every 1 second. 

![screenshot](https://cloud.githubusercontent.com/assets/3138533/17652244/ef0979e8-623c-11e6-81ff-0bbe14371607.png)
![sensor](https://cloud.githubusercontent.com/assets/3138533/17652231/b828a084-623c-11e6-8484-29ad086bcdfb.jpg)
![pins](https://cloud.githubusercontent.com/assets/3138533/17652232/b8352c96-623c-11e6-92f1-e0b3ec6d558a.jpg)

