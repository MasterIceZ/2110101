def process(s: str):
  res = dict()
  for x in s.lower():
    if not x.isalpha():
      continue
    if x not in res:
      res[x] = 1
    else:
      res[x] += 1
  return res

def getDiff(dict_1: dict, dict_2: dict):
  response = list()
  for x in sorted(dict_1):
    diff = dict_1[x] - (dict_2[x] if x in dict_2 else 0)
    if diff > 0:
      response.append(" - remove {} {}{}".format(diff, x, "" if diff == 1 else "'s"))
  if len(response) != 0:
    return response
  return [" - None"]

a = input()
b = input()

count_dicts = [process(a), process(b)]
print(a)
print("\n".join(getDiff(count_dicts[0], count_dicts[1])))
print()
print(b)
print("\n".join(getDiff(count_dicts[1], count_dicts[0])))
