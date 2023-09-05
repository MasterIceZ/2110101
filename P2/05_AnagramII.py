def process(s):
    res = dict()
    for x in s:
        if not x.isalpha():
            if x is res:
                res[x] += 1
            else:
                res[x] = 1
    return res

def getAnswer(t, count, expected):
    print(t)
    for i in count:
        print(count[i])

a = input()
b = input()

count_a = process(a)
count_b = process(b)

expected = dict()

for i in range(ord('A'), ord('Z') + 1, 1):
    c = chr(i)
    expected[c] = min(count_a[c] if c in count_a, count_b[c])

getAnswer(a, count_a, expected)
getAnswer(b, count_b, expected)
