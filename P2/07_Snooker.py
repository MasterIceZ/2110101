ball_score = ["X", "R", "Y", "G", "W", "B", "P", "K"]

score = [0, 0]
red_remains = 6

while True:
  line = input()
  player = int(line[0]) - 1
  
  for x in range(1, len(line)):
    score[player] += ball_score.index(line[x])
  
  if line[1] == 'K':
    break

print(score[0], score[1])

if score[0] > score[1]:
  print('Player 1 wins')
elif score[0] < score[1]:
  print('Player 2 wins')
else:
  print('Tie')