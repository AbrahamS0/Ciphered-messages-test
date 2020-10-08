#programa que re crea un stream cipher
key = 183
plaintext= "a"
ptd = ord(plaintext)
cip = ptd^key
print "Letra encriptada : ", cip
p2= cip^key
print "Letra des encriptada: ", p2
