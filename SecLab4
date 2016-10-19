from Crypto.Cipher import AES
import hashlib
import sys
import binascii

key = '1234567812345678'
plaintext = 'AAAABBBBCCCCDDDDAA'

def encrypt(data,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(data))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

def addPadding(data):
    length =  16 - (len(data) % 16)
    data += "\x00" * (length)
    return data

def removePadding(data):
    
    return data

print(plaintext)

plaintext = addPadding(plaintext)
hextext = plaintext.encode("hex")

print(hextext)

ciphertext = encrypt(hextext,key,AES.MODE_ECB)

print(ciphertext)

hextext = decrypt(ciphertext,key,AES.MODE_ECB)

hextext.strip("0")

plaintext = hextext.decode("hex")

print(plaintext)