def getDay(a, b, c):
    m_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return c * 365 + sum(m_d[0:b-1]) + a

bd, bm, by, d, m, y = [int(e) for e in input().split()]

b_days = getDay(bd, bm, by)
a_days = getDay(d, m, y)

diff = abs(a_days - b_days)
print(diff)
