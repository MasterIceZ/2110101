line = list()
score_dict = dict()
ota_dict = dict()
kami_dict = dict()

def answer(l):
  l.sort()
  l.reverse()
  print("{}, {}, {}".format(l[0][1], l[1][1], l[2][1]))

def score():
  l = list()
  for x in score_dict:
    l.append([score_dict[x], x])
  answer(l)

def ota():
  l = list()
  for x in ota_dict:
    l.append([len(ota_dict[x]), x])
  answer(l)

def kami():
  d = dict()
  for x in kami_dict:
    k = None
    s = 0
    for y in kami_dict[x]:
      if kami_dict[x][y] > s:
        k = x
        s = kami_dict[x][y]
      elif kami_dict[x][y] == s:
        if y < k:
          k = y
    if k is not None:
      d[k] = d.get(k, 0)
      d[k] += 1
  for x in score_dict.keys():
    if x not in d:
      d[x] = 0
  l = list()
  for x in d:
    l.append([d[x], x])
  answer(l)

while len(line) != 1:
  line = input().split()
  if len(line) == 1:
    if line[0] == "1":
      score()
    elif line[0] == "2":
      ota()
    elif line[0] == "3":
      kami()
    break
  score_dict[line[1]] = score_dict.get(line[1], 0)
  score_dict[line[1]] += int(line[2])

  ota_dict[line[1]] = ota_dict.get(line[1], set())
  ota_dict[line[1]].add(line[0])

  kami_dict[line[0]] = kami_dict.get(line[0], dict())
  kami_dict[line[0]][line[1]] = kami_dict[line[0]].get(line[1], 0)
  kami_dict[line[0]][line[1]] += int(line[2])  