def factor(N):
  factors = list()
  cnt = 0
  while N % 2 == 0:
    N //= 2
    cnt += 1
  if cnt > 0:
    factors.append([2, cnt])
  i = 3
  while i * i < N:
    cnt = 0
    while N % i == 0:
      N //= i
      cnt += 1
    if cnt != 0:
      factors.append([i, cnt])
    i += 2
  if N > 2:
    factors.append([N, 1])
  return factors

exec(input().strip())