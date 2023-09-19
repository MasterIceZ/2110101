line = input()
i = 0
plays = list()

while i < len(line):
  if len(plays) == 9:
    cur = list()
    for x in line[i:]:
      if x == 'X':
        cur.append(10)
      elif x == '/':
        cur.append(10 - cur[-1])
      else:
        cur.append(int(x))
    plays.append(cur)
    break
  elif line[i] == 'X':
    plays.append([10])
  elif line[i + 1] == '/':
    plays.append([int(line[i]), 10 - int(line[i])])
    i += 1
  else:
    plays.append([int(line[i]), int(line[i + 1])])
    i += 1
  i += 1

# print(plays)

all_scores = list()
for x in plays:
  for y in x:
    all_scores.append(y)

scores = list()
sum_size = 0

for i in range(9):
  current_score = sum(plays[i])
  current_len = len(plays[i])
  if current_score == 10:
    if len(plays[i]) == 1:
      current_score += all_scores[sum_size + current_len] + all_scores[sum_size + current_len + 1]
    else:
      current_score += all_scores[sum_size + current_len]
  scores.append(current_score)
  sum_size += current_len
scores.append(sum(plays[9]))

q = int(input())
if 1 <= q <= 10:
  print(scores[q - 1])
else:
  print(sum(scores))