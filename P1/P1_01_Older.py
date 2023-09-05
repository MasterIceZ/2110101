to_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

a = input().split()
b = input().split()

if a[1:] == b[1:]:
    print(a[0], b[0])
elif int(a[-1]) != int(b[-1]):
    if int(a[-1]) < int(b[-1]):
        print(a[0])
    else:
        print(b[0])
elif to_month.index(a[1]) != to_month.index(b[1]):
    if to_month.index(a[1]) < to_month.index(b[1]):
        print(a[0])
    else:
        print(b[0])
else:
    date_a = int(a[2].split(',')[0])
    date_b = int(b[2].split(',')[0])

    if date_a < date_b:
        print(a[0])
    else:
        print(b[0])
