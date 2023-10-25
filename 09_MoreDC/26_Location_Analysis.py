n = int(input())

locations = dict()
users = list()

for _ in range(n):
  line = input()
  t = line.split(':')
  
  user = t[0]
  cities = t[1].strip().split(", ")

  users.append(user)
  for city in cities:
    if user not in locations:
      locations[user] = set()
    locations[user].add(city)

f = input()
answer = list()

for user in users:
  if user == f:
    continue
  inter = locations[f].intersection(locations[user])
  if len(inter) != 0:
    answer.append(user)
if len(answer) > 0:
  print("\n".join(answer))
else:
  print("Not Found")