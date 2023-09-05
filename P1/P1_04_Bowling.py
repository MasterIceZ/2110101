line = input()

scores = [0 for i in range(0, 10, 1)]
current_idx = 0

for i in range(0, 9, 1):
    if line[current_idx] == 'X':
        scores[i] = "STRIKE"
    elif line[current_idx + 1] == '/':
        scores[i] = "SPARE"
        current_idx += 1
    else:
        scores[i] = int(line[current_idx]) + int(line[current_idx + 1])
        current_idx += 1

    current_idx += 1


