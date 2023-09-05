def str2RLE(l):
    last = l[0]
    cnt = 1
    res = list()
    for i in range(1, len(l)):
        if l[i] == last:
            cnt += 1
        else:
            print(last, cnt, end=" ")
            cnt = 1
        last = l[i]
    print(last, cnt)

def RLE2str(l):
    res = str()
    for i in range(0, len(l), 2):
        res += l[i] * int(l[i + 1])
    print(res)

mode = input()

if mode == "str2RLE":
    str2RLE(input())
elif mode == "RLE2str":
    RLE2str(input().split())
else:
    print("Error")
