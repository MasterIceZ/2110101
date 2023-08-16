num = int(input())

answer = str()

if num >= 10**10:
    answer = str(round(num / 10**9)) + "B"
elif num >= 10**9:
    answer = str(round(num / 10**9, 1)) + "B"
elif num >= 10**7:
    answer = str(round(num / 10**6)) + "M"
elif num >= 10**6:
    answer = str(round(num / 10**6, 1)) + "M"
elif num >= 10**4:
    answer = str(round(num / 10 ** 3)) + "K"
elif num >= 10**3:
    answer = str(round(num / 10**3, 1)) + "K"
else:
    answer = str(num)

print(answer)
