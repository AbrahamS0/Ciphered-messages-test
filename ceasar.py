key = 'abcdefghijklmnopqrstuvwxyz'

def ceasar_cipher(plaintext, n):
    cip=''
    plaintext=plaintext.lower()
    for x in plaintext:
        if x.isalpha():
            cip=cip + key[(key.index(x)+n)%26]
        else:
            cip+=x
    return cip

def ceasar_decipher(ciphertext, n):
    plain=''
    ciphertext=ciphertext.lower()
    for x in ciphertext:
        if x.isalpha():
            plain=plain + key[(key.index(x)-n)%26]
        else:
            plain+=x
    return plain

cifrado=ceasar_cipher("Hola a todo el mundo van a sacar todos 100",5)
print cifrado
descifrado = ceasar_decipher(cifrado,5)
print descifrado
