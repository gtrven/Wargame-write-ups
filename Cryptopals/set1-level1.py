import binascii
import base64
#use binascii.hexlify() to encode in hex
#use binascii.unhexlify() to hex decode
#use base64.b64encode() to base64 encode something

#Level 1: Convert hex to base64.
#If you enter in: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#then you should get: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t


def hexToBase64(s):
    decoded = binascii.unhexlify(s)
    return base64.b64encode(decoded).decode('ascii')

hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

print(hexToBase64(hexString))
