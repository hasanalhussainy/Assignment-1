import socket
import datetime
Host="Localhost"
Server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address=(Host, 5555)
Server.bind(server_address)
now=datetime.datetime.now()
while True : 
    data , address= Server.recvfrom(2048)
    print ("%s bytes received from %s is" % (len(data), address)) 
    print(now)
    if data:
        sent = Server.sendto(data, address)
