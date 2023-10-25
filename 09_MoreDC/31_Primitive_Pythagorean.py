def gcd(a,b):
  while b != 0:
    a,b = b, a%b
  return a

def is_coprime(a, b, c):
  return gcd(gcd(a, b), c) == 1

def primitive_Pythagorean_triples(max_len):
  triple = []
  for c in range(1, max_len+1):
    for a in range(1, c):
      b = (c * c - a * a) ** 0.5
      if b < a:
        break
      if b // 1 == b and is_coprime(a, int(b), c):
        triple += [[a, int(b), c]]
  return triple
exec(input().strip()) 