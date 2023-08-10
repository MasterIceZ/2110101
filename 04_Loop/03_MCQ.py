sol = input()
ans = input()

if len(sol) != len(ans):
    print("Incomplete answer")
else:
    print(sum([1 if sol[i] == ans[i] else 0 for i in range(len(sol))]))
