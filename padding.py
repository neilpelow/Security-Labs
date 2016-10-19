from Crypto.Cipher import DES
import hashlib
import sys
import binascii

key = '12345678'
plaintext = 'AAAABBBBCCCC'

def encrypt(data,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(data))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))

def addPadding(data):
    length =  8 - (len(data) % 8)
    data += "\x00" * (length)
    return data

def removePadding(data):
    
    return data

print(plaintext)

plaintext = addPadding(plaintext)
hextext = plaintext.encode("hex")

print(hextext)

ciphertext = encrypt(hextext,key,DES.MODE_ECB)

print(ciphertext)

hextext = decrypt(ciphertext,key,DES.MODE_ECB)

hextext.strip("0")

plaintext = hextext.decode("hex")

print(plaintext)