n = int(input())

a = list()
answer = -1
one = False

for i in range(n):
    a.append(int(input()))
   
i = 1
while i < n:
    if a[i] - a[i - 1] != a[1] - a[0]:
        if answer == -1:
            answer = i + 1
            i += 1
        else:
            one = True

    i += 1
print(1 if one else answer)
