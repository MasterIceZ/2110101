n = int(input())

a = list()

for i in range(n):
    a.append([int(i) for i in input().split()])

operation = input()

if operation == "Zig-Zag":
    state = 0
else :
    state = 1

min_list = list()
max_list = list()

for i in range(n):
    
    min_list.append(a[i][state])
    max_list.append(a[i][(state + 1) % 2])

    state = (state + 1) % 2

print(min(min_list), max(max_list))
