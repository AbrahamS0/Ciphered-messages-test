from socket import *

print "Simple port scanner"
print "-------------------"
print ""
adress = input("Enter adress (or localhost): ")
ip = gethostbyname(adress)
print adress,"has the IP:",ip
alpha = int(input("Port (min):"))
omega = int(input("Port (max):"))


def scanner(ip,alpha, omega):
    count = 0
    for ports in range(alpha, omega):
        try:
            print "Scanning port :%d" % (ports,)
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(3)
            s.connect((ip, ports))
            print "Port %d: is OPEN" % (ports,)
            count = count + 1
        except:
            print "Port %d is CLOSED" % (ports,)
        s.close()
    print "Scanning finshed !"
    print ""
    print "Found %d open ports" % (count)




print ""
print "Beggin to scan..."
scanner(ip,alpha,omega)
