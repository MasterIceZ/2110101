s = sorted([int(x) for x in input().split()])

l = [s[0]]
last = s[0]

for i in range(1, len(s)):
    if s[i] != last:
        l.append(s[i])
    last = s[i]

print(len(l))

if len(l) > 10:
    l = l[:10]
    
print(l)
