from socket import *
from ex import *
import threading
import os
key=183

host="127.0.0.1"            #Direccion ip a conectarse
port=4448 
def envia_datos(s):

    return

def recibe_datos(q):
    while 1:
        msg=q.recv(1024)
        if (msg.strip().decode('ascii')=='q'):
            os._exit(0)
        print ("Message from client : " + msg.strip().decode('ascii'))
        decip=decrypt_stream(msg,key)
        print "Message decoded: ", decip
    return

s=socket(AF_INET, SOCK_STREAM)       #Creando un socket de conexion
s.connect((host,port))              # Conectandose a la ip y puerto
print "Chat connected, enter data to be sent: "
t = threading.Thread(target=recibe_datos,args=(s,))
t.start()
while 1:
    data=input("Client typing: >  \n")
    if (data=='q' or data== 'Q'):
        s.send('q')
        s.close()
        os._exit(0)
    elif (data=="clearscreen"):
        os.system("clear")
    else:
        ciph=encrypt_stream(data,key)                                        # user
        s.send(ciph)
