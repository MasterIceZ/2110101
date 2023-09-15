def printAnswer(arr):
  for x in arr:
    print(x)

def flip(arr):
  global n
  response = list()
  for i in range(0, n):
    response.append(arr[i][::-1])
  return response

def rotate90(arr):
  global n
  m = len(arr[0])
  response = list()
  for i in range(0, m):
    response.append(''.join(arr[j][i] for j in range(n - 1, -1, -1)))
  return response

def rotate180(arr):
  global n
  response = list()
  for i in range(n-1, -1, -1):
    response.append(arr[i][::-1])
  return response

degree = input().strip()
arr = list()
ok = True

n = int(input().strip())
for i in range(n):
  arr.append(input().strip())

for i in range(1, n):
  if len(arr[i]) != len(arr[0]): 
    ok = False

if not ok:
  print("Invalid size")
elif degree == 'flip':
  arr = flip(arr)
  printAnswer(arr)
elif degree == '90':
  arr = rotate90(arr)
  printAnswer(arr)
elif degree == '180':
  arr = rotate180(arr)
  printAnswer(arr)
