line = input()

a = str()
b = str()

for i in range(3, len(line), 7):
    a += line[i]

for i in range(7, len(line), 5):
    b += line[i]

c = str(int(a) + int(b) + 10000)[::-1][1:4][::-1]
d = int(str(sum([int(x) for x in c]))[-1])

d = chr(ord('A') + d)

print(c + d)
