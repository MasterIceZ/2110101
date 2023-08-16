a = float(input())

def binarySearch(l, r):
    while l < r:
        mid = (l + r) / 2.0
        v = 10 ** mid
        if abs(v - a) < 1e-9:
            return mid
        elif v > a:
            r = mid - 1e-9
        else:
            l = mid + 1e-9
    return l

print(round(binarySearch(0, a), 6))
