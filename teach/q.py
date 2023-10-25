s = input().split()
print(" ".join([s[0][0] + s[-1][1:]] + s[1:-1] + [s[-1][0] + s[0][1:]]))