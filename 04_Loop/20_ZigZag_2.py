min_1 = 0
max_1 = 0
min_2 = 0
max_2 = 0

i = 0

while True:
    s = input()
    if s == 'Zig-Zag' or s == 'Zag-Zig':
        if s == 'Zig-Zag':
            print(min_2, max_1)
        else:
            print(min_1, max_2)
        break
    else:
        x = int(s.split()[0])
        y = int(s.split()[1])
        if i == 0:
            min_1 = x
            max_1 = x
            min_2 = y
            max_2 = y
        else:
            min_1 = min(min_1, x)
            max_1 = max(max_1, x)
            min_2 = min(min_2, y)
            max_2 = max(max_2, y)
    i += 1
