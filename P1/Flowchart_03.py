import math

x = input().split()
a, b, c, d = int(x[0]), int(x[1]), int(x[2]), int(x[3])

if a == 1:
  c, d = d, c
  if b == 1:
    c = c + d
  elif b == 2:
    c = c - d
  elif b != 3:
    c = c + c ** d
  else:
    c = c / d
  a = (d + ((c / b) ** 3 + d) ** 0.5) / (2 + b * d)
else:
  if a == 2:
    if b > 1:
      c = c + d
    if b > 2:
      c = c / d
    if b > 3:
      c = c + c ** d
    else:
      a = math.log(c, 10)
  else:
    while a > d:
      a = a - 2
      if a < b:
        break
      c = c + a
      
print(a, b, c, d)