u = [float(i) for i in input()[1:-1].split(", ")]
v = [float(i) for i in input()[1:-1].split(", ")]

res = list()

for i in range(len(u)):
    res.append(u[i] + v[i])
print(u, "+", v, "=", res)
