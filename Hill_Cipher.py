import math
t = 0
count = 0
keySize = int(input())
HillMatrix = [[0]*int(math.sqrt(keySize)) for i in range(int(math.sqrt(keySize)))]
temp = list(map(int, input().strip().split(' ')))
for i in range(int(math.sqrt(keySize))):
    for j in range(int(math.sqrt(keySize))):
        HillMatrix[i][j] = temp[count]
        count = count + 1
Encrypt = input()
while t < len(Encrypt):
    EncryptMatrix = [['X']*1 for i in range(int(math.sqrt(keySize)))]
    result = [[0]*1 for i in range(int(math.sqrt(keySize)))]
    for i in range(int(math.sqrt(keySize))):
        if t < len(Encrypt):
            EncryptMatrix[i][0] = Encrypt[t]
            t = t + 1
    for i in range(len(HillMatrix)):
        for j in range(len(EncryptMatrix[0])):
            for k in range(len(EncryptMatrix)):
                result[i][j] += HillMatrix[i][k] * (ord(EncryptMatrix[k][j])-65)
    for i in range(int(math.sqrt(keySize))):
        result[i][0] = chr((result[i][0] % 26) + 65)
        print(result[i][0],end='')
