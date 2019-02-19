opSize = int(input())
p_table = []
ip_array = []
p_table.append(input().split())
ipSize = int(input())
x = opSize
y = ""
ip = bin(int(input(), 16))[2:]
ip_len = len(ip)

for i in range(ipSize):
    ip_array.append(0)

for i in range(ip_len):
    ip_array[ipSize-1] = ip[ip_len - 1]
    ipSize = ipSize - 1
    ip_len = ip_len - 1

for i in range(x):
    y += str(ip_array[int(p_table[0][i]) - 1])

print(hex(int(y, 2)).upper()[2:])

