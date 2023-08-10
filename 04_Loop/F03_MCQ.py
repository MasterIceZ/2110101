def grade_mcq(sol, ans):
    if len(sol) != len(ans):
        return -1
    return sum([1 if sol[i] == ans[i] else 0 for i in range(0, len(ans), 1)])

exec(input())
