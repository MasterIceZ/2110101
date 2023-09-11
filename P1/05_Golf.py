import math

pars = list()
strokes = list()
fix_strokes = list()

for i in range(1, 10, 1):
    par, stroke, cal = [int(x) for x in input().split()]
    
    pars.append(par)
    strokes.append(stroke)
    if cal == 1:
        fix_strokes.append(min(stroke, par + 2))

handicap = int(math.floor(0.8 * (1.5 * sum(fix_strokes) - sum(pars))))

print(sum(strokes))
print(handicap)
print(sum(strokes) - handicap)
