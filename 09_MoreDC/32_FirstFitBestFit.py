def first_fit(L, e):
  for i in range(len(L)):
    if sum(L[i]) + e > 100:
      continue
    L[i].append(e)
    return 
  L.append([e])

def best_fit(L, e):
  best_sum = 0
  idx = -1
  for i in range(len(L)):
    s = sum(L[i]) + e
    if s > 100 or s <= best_sum:
      continue
    best_sum = s
    idx = i
  if idx != -1:
    L[idx].append(e)
  else:
    L.append([e])

def partition_FF(D):
  res = list()
  for x in D:
    first_fit(res, x)
  return res

def partition_BF(D):
  res = list()
  for x in D:
    best_fit(res, x)
  return res

exec(input().strip())