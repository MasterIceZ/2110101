s = input()

charactors = list()
frequency = list()
last_charactor = '!'
count = 0

def update(char, cnt):
    charactors.append(char)
    frequency.append(cnt)

for i in range(len(s)):
    
    if s[i] == last_charactor:
        count += 1
    else:
        update(last_charactor, count)
        count = 1

    last_charactor = s[i]
update(last_charactor, count)

for i in range(1, len(charactors)):
    print(charactors[i], frequency[i], end=" ")
