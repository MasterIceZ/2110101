s = input().strip().lower()

c = dict()
for x in s:
  if not x.isalpha():
    continue
  if x in c:
    c[x] += 1
  else:
    c[x] = 1

l = list()
for x in c:
  l.append([-c[x], x])

l = sorted(l)
for x in l:
  print(x[1], '->', -x[0])