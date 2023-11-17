import numpy as np

def mult_table(nrows, ncols):
  shape = (nrows, ncols)
  res = np.arange(nrows * ncols).reshape(shape)

  for i in range(0, nrows):
    for j in range(0, ncols):
      res[i, j] = (i + 1) * (j + 1)

  return res

exec(input().strip())