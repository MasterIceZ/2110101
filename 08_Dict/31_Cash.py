def total(pocket):
  return sum([pocket[x] * x for x in pocket])

def take(pocket, money_in):
  for m in money_in:
    if m in pocket:
      pocket[m] += money_in[m]
    else:
      pocket[m] = money_in[m]
  return pocket

def pay(pocket, amt):
  l = sorted(pocket.keys(), reverse=True)
  res = dict()
  for x in l:
    if amt >= x * pocket[x]:
      amt -= x * pocket[x]
      res[x] = pocket[x]
    elif x <= amt:
      res[x] = amt // x
      amt = amt % x
  if amt != 0:
    return {}
  for x in res:
    pocket[x] -= res[x]
  return res

exec(input().strip()) 