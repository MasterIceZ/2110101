d = dict()
n = int(input())
l = dict()

for i in range(n):
  k = input()
  s = input().split()
  d[k] = dict()
  for x in s:
    if x not in d[k]:
      d[k][x] = 0
    d[k][x] += 1
  l[k] = len(s)
while True:
  s = input()
  if s == "-1":
    break
  answer = None
  rate = 0
  for x in d:
    if s in d[x]:
      if answer == None:
        answer = x
        rate = d[x][s] / l[x]
      elif rate < d[x][s] / l[x]:
        rate = d[x][s]
        answer = x
  if answer is None:
    print("NOT FOUND")
  else:
    print(answer)