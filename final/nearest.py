import numpy as np

def nearest(D, x):
    return D[np.argmin(D - x, axis=0)]

print(nearest(np.array([3.1, 2.2, 4.5, 9.0]), 2.1))
