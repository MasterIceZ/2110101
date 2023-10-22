def convex_polygon_area(p):
  p.append(p[0])
  res = 0
  for i in range(len(p)-1):
    res += (p[i][0] * p[i + 1][1] - p[i][1] * p[i + 1][0])
  return abs(res) / 2

def is_heterogram(s):
  t = s
  t = t.upper()
  for x in t:
    if x.isalpha() and t.count(x) > 1:
      return False
  return True

def replace_ignorecase(s, a, b):
  idx = 0
  while idx < len(s):
    l = s.lower().find(a.lower(), idx)
    if l == -1:
      return s
    s = s[:l] + b + s[l+len(a):]
    idx = l + len(b)
  return s

def top3(votes):
  res = list()
  t = list()
  for vote in votes:
    t.append([-votes[vote], vote])
  for x in sorted(t):
    res.append(x[1])
    if len(res) == 3:
      return res
  return res

for k in range(2):
    exec(input().strip())
