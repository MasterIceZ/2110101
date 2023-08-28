n = int(input())
p = 1

print("." * (n - 1) + "*")

for i in range(n - 2, 0, -1):
    print("." * i + "*" + "." * p + "*")
    p += 2

print("*" * (p + 2))
