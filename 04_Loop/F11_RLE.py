def RLE(t):
    charactors = list()
    frequency = list()
    last_charactor = '!'
    count = 0

    def update(char, cnt):
        charactors.append(char)
        frequency.append(cnt)

    for i in range(len(t)):
        if t[i] == last_charactor:
            count += 1
        else:
            update(last_charactor, count)
            count = 1

        last_charactor = t[i]
    
    update(last_charactor, count)

    return [[charactors[i], frequency[i]] for i in range(1, len(charactors))]


exec(input())
