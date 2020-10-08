
#programa que re crea un stream cipher
import binascii
key = 183
plaintext= "Esto es un mensaje altamente confidencial"


def encrypt_stream(plaintext,key):
    ciphered=''
    for x in plaintext:
        ptd=ord(x)
        cip=ptd^key
        ciphered=ciphered+chr(cip)
    return binascii.hexlify(ciphered)

def decrypt_stream(ciphered,key):
    ciphered=binascii.unhexlify(ciphered)
    plain=''
    for x in ciphered:
        ctd=ord(x)
        descip=ctd^key
        plain=plain+chr(descip)
    return plain

print "Original text: ",plaintext
ciph=encrypt_stream(plaintext,key)
print "Ciphered text: ",ciph
decip=decrypt_stream(ciph,key)
print "Deciphered text: ",decip
