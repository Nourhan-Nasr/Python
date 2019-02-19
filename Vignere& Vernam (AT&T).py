key = input()
Encrypt = input()
keyLength = len(key)
Vigenere = ''
Vernam = ''
j = 0
for i in range(len(Encrypt)):
    if j < keyLength:
        Vigenere += chr(((ord(Encrypt[i])+ord(key[j])) % 26)+65)
        j = j + 1
    else:
        j = 0
        Vigenere += chr(((ord(Encrypt[i])+ord(key[j])) % 26)+65)
        j = j + 1
print("Vigenere:", Vigenere)
j = 0
for i in range(len(Encrypt)):
    if j < keyLength:
        Vernam += "0x{:02x}".format(ord(Encrypt[i]) ^ ord(key[j])).upper()[2:]
        j = j + 1
    else:
        j = 0
        Vernam +=  "0x{:02x}".format(ord(Encrypt[i]) ^ ord(key[j])).upper()[2:]
        j = j + 1
print("Vernam:", Vernam)
if len(Encrypt) == len(key):
    print("One-Time Pad: YES")
else:
    print("One-Time Pad: NO")
    
