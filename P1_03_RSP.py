one_win = ["P R", "S P", "R S"]
two_win = ["R P", "P S", "S R"]

one = 0
two = 0
tie = 0

n = int(input())

for i in range(3 * n):
    line = input()

    if line in one_win:
        one += 1
    elif line in two_win:
        two += 1
    else:
        tie += 1

    if one >= n or two >= n:
        if one > two:
            winner = one
        else:
            winner = two

print(one, two)

if tie > one and tie > two:
    print("Tie")
elif one > tie and one > two:
    print("Player 1 wins")
else:
    print("Player 2 wins")
