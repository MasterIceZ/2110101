root = dict()
have = set()

# disjoint set union
def find_root(u):
  if u == root[u]:
    return u
  root[u] = find_root(root[u])
  return root[u]

def init_node(x):
  if x not in have:
    have.add(x)
    root[x] = x 
    root["ENEMY!!!" + x] = "ENEMY!!!" + x

while True:
  line = input()
  if line == 'End':
    break
  line = line.split()
  if line[0] == 'Ally':
    a = line[1]
    b = line[2]
    init_node(a)
    init_node(b)
    root_a = find_root(a)
    root_b = find_root(b)
    root[root_a] = root_b
  elif line[0] == 'Enemy':
    a = line[1]
    b = line[2]
    init_node(a)
    init_node(b)
    root_a = find_root(a)
    root_b = find_root(b)
    enemy_root_a = find_root("ENEMY!!!" + a)
    enemy_root_b = find_root("ENEMY!!!" + b)
    root[enemy_root_b] = root_a
    root[enemy_root_a] = root_b
  else:
    ok = True
    line = line[1:]
    for i in range(0, len(line)):
      a = line[i]
      b = line[(i + 1) % len(line)]
      init_node(a)
      init_node(b)
      print(find_root(a), find_root(b), find_root("ENEMY!!!" + a), find_root("ENEMY!!!" + b))
      if find_root(a) != find_root("ENEMY!!!" + b) or find_root(b) != find_root("ENEMY!!!" + a):
        ok = False
    print("Okay" if ok else "No")
