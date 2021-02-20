import socket
import time



print ("Enter Your Server Adress Followed By the Port")
host= str(input("Adress:"))
port= int(input("Port:"))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address=(host,port)

sum=1
    


for i in range (5)  : 
    message = "Test message. This will be echoed" 
    print ("Sending %s" % message) 
    t1=time.time()
    sent = sock.sendto(message.encode('utf-8'), server_address)
    # Receive response 
    data, server = sock.recvfrom(2048)
    t2= time.time()
    print ("received %s" % data)
    tim = float(t2-t1)
    print (tim)
    sum+= tim
    
average= sum/5
print ('Average:' , average , "  s")