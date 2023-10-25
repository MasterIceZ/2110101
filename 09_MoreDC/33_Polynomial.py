def get_mono(poly):
  response = dict()
  for mono in poly:
    response[mono[1]] = mono[0]
  return response


def add_poly(p1, p2):
  response = list()
  
  p1_mono = get_mono(p1)
  p2_mono = get_mono(p2)

  degrees = set()
  for x in p1_mono:
    degrees.add(x)
  for x in p2_mono:
    degrees.add(x)
  sorted_degrees = sorted([x for x in degrees], reverse=True)
  
  for deg in sorted_degrees:
    r = 0
    if deg in p1_mono:
      r += p1_mono[deg]
    if deg in p2_mono:
      r += p2_mono[deg]
    if r != 0:
      response.append((r, deg))

  return response

def mult_poly(p1, p2):
  response = list()

  p1_mono = get_mono(p1)
  p2_mono = get_mono(p2)

  for x in p2_mono:
    current = list()
    for y in p1_mono:
      current.append((p1_mono[y] * p2_mono[x], x + y))
    response = add_poly(response, current)
  return response

for i in range(3):
  exec(input().strip())