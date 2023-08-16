a = float(input())

l = 0
x = a
r = 0

while x > 0:
    r += 1
    x /= 10

def search(l, r):
    while l < r:
        mid = (l + r) / 2

        v = 10.0 ** mid

        if abs(v - a) < 1e-10:
            return mid
        
        if v > a:
            r = mid - 1e-10
        else:
            l = mid + 1e-10
    return l

print(round(search(l, r), 6))
