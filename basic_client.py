#Client
#TCP Client code

from socket import *
import threading

host = "127.0.0.1"    #Direccion ip a conectarse
port = 1501         #Puerto a conectarse

s = socket(AF_INET, SOCK_STREAM)     #Creando socket de conexion
s.connect((host, port))#Concetandose a la ip puerta

t = threading.Thread(target=recibe, args=(s,))
t.start

def envia(s,q):
    data = input("Enter data to be send: ")
    s.send(data)
    
def recibe(s):
    while 1:
        msg = s.recv(1024)       #Recibiendo hasta 1024 bytes y guardando en ms
        print ("Message from server : " + msg.strip().decode('ascii'))
    



              #Cerrando el socket
