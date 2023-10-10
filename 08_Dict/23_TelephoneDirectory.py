n = int(input())
d = dict()
for i in range(n):
  s = input().split()
  d[s[0] + " " + s[1]] = s[2]
  d[s[2]] = s[0] + " " + s[1]

q = int(input())
for i in range(q):
  s = input()
  print(s, '--> ', end="")
  if s in d:
    print(d[s])
  else:
    print("Not found")