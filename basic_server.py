#Server
#TCP Server code
from socket import *
import threading


host = "127.0.0.1"
port = 1501
#Imports socket module
s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))            #Binds the socket. Note that the input to
s.listen(1)
q, addr=s.accept()
print "listening for connections... "
print "Enter data to be sent: "
t = threading.Thread(target=recibe, args=(q,))
t.start()
#MANDAR
def envia(s):
    return
"""while True:
    data = raw_input ("Enter data to be send: ")
    q.send(data)"""
    
#Recibir   
def recibe(q):
    while 1:
        msg = q.recv(1024)
        print ("Message from client : " + msg.strip().decode('ascii'))
    



