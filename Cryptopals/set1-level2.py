import binascii
import base64
#use binascii.hexlify() to encode in hex
#use binascii.unhexlify() to hex decode
#use base64.b64encode() to base64 encode something

#Challenge 2: fixed XOR. 

#If you feed it the string "1c0111001f010100061a024b53535009181c", 
#and xor it against "686974207468652062756c6c277320657965" after hex decoding, 
#it should produce "746865206b696420646f6e277420706c6179"

def xor(b1, b2):
	b = bytearray(len(b1))
	for i in range(len(b1)):
		b[i] = b1[i] ^ b2[i]
	return b


x = "1c0111001f010100061a024b53535009181c"
y = "686974207468652062756c6c277320657965"
x = binascii.unhexlify(x)
y = binascii.unhexlify(y)

print(binascii.hexlify(xor(x, y)))
