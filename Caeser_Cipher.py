key = int(input()) % 26
x = input()
for i in range(len(x)):
    if ord(x[i])+key <= 90:
        print(chr(ord(x[i])+key),end='')
    else:
        print(chr((ord(x[i])+key) % 90 + 64),end='')
    
