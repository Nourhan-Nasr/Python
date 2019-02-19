size = int(input())
p_table = []
p_sort = []
x = 0
flag = 0

p_table.append(input().split())

for i in range(size):
    p_table[0][i] = int(p_table[0][i])

for i in range(size):
        if i+1 in p_table[0]:
            p_sort.append(p_table[0].index(i+1) + 1)
        else:
            p_sort.append(0)

p_table[0].sort()

for i in range(1, size):
    if p_table[0][x] == p_table[0][i] or abs(p_table[0][x] - p_table[0][i]) != 1:
        print("IMPOSSIBLE")
        flag = 1
        break
    x = x + 1

if flag == 0:
    for i in range(size):
        print(p_sort[i], end=" ")

