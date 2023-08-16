u = [float(i) for i in input()[1:-1].split(', ')]
v = [float(i) for i in input()[1:-1].split(', ')]
print(u, "+", v, "=", [u[i] + v[i] for i in range(len(u))])
