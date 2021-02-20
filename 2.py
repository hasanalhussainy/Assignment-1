import socket
import time
print ("Please enter the server and its port")
Server= str(input("The Server is:"))
port= int(input("The Port is:"))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Server_Address=(Server,port)
S=0
for i in range (5)  : 
    MSG = "This message will be echoed" 
    print ("Send %s" % MSG) 
    T1=time.time()
    sent = sock.sendto(MSG.encode('utf-8'), Server_Address)
    data, server = sock.recvfrom(2048)
    T2= time.time()
    print ("received %s" % data)
    finaltime = float(T2-T1)
    print (finaltime)
    S+= finaltime
#We can find the averafe now
average= S/5
print ('The final Average is :' , average , "  s")