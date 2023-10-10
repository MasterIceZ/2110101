s = input().strip().upper()

ok = True
for x in s:
  if x not in "ATCG":
    ok = False
    break

t = input().strip()

if not ok:
  print('Invalid DNA')
elif t == 'R':
  r = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
  print(''.join([r[x] for x in s][::-1]))
elif t == 'F':
  print("A={}, T={}, G={}, C={}".format(s.count('A'), s.count('T'), s.count('G'), s.count('C')))
else:
  u = input().strip()
  res = 0
  for i in range(len(s) - len(u) + 1):
    res += (s[i:i+len(u)] == u)
  print(res)