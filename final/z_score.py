import numpy as np

def z_score(X):
    return np.array((X - np.mean(X)) / np.std(X))

print(z_score(np.array([1, 2])))
