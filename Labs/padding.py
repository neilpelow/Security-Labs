from Crypto.Cipher import DES
import hashlib
import sys
import binascii

key = '12345678'
plaintext = 'AAAABBBBCCCC'

def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))

textLength = len(plaintext) 

print"Plaintext: ", (plaintext)

if textLength > 8:
    padLength = textLength % 8
else:
	padLength = 8 + textLength
	padLength = padLength/2

strPadLength = str(padLength)

plaintext = binascii.hexlify(plaintext)

for x in range(0, padLength):
    	plaintext = plaintext + "0" + strPadLength

ciphertext = encrypt(plaintext,key,DES.MODE_ECB)

print "Plaintext length before padding:", (textLength)

print "Padding added:", (padLength)

print "Plaintext after padding:", (plaintext)
print "/Encrypted Ciphertext:", (ciphertext)

ciphertext = decrypt(ciphertext, key, DES.MODE_ECB)

print "Decrypted Ciphertext:", (ciphertext)

#length of plaintext
#if length > 8 then 8 % length of plaintext
#else length < 8 then 8 - length of plaintext
#pad_length = 8 - length of plaintext
# and put pad_len in double digit format so 4 - 04
#pad_length * 2 becusae of double digit 
#zfile function to fill string to 0000003035 fills strings with 0's
#then add padded_text 0000003035 to hex of plaintext
#print value so - JH4K54H4J65KJH56H60000003035 