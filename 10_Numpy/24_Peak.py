import numpy as np
def peak_indexes(x):
  left_of_this = np.concatenate((x[1:], [9999999]))
  right_of_this = np.concatenate(([9999999], x[:-1]))
  return list(np.where((x > left_of_this) & (x > right_of_this))[0])

def main():
  d = np.array([float(e) for e in input().split()])
  pos = peak_indexes(np.array(d))
  if len(pos) > 0:
    print(", ".join([str(e) for e in pos]))
  else:
    print("No peaks")

exec(input().strip())