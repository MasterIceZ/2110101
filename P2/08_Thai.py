d = { 0: "soon", 1: "neung", 2: "song", 3: "sam", 4: "si", 5: "ha", 6: "hok", 7: "chet", 8: "paet", 9: "kao" }

def to_Thai(N):
    if len(str(N)) == 1:
        return d[N]

    response = list()

    if N >= 1000:
        response.append(d[N // 1000])
        response.append("pun")
        N %= 1000
    if N >= 100:
        response.append(d[N // 100])
        response.append("roi")
        N %= 100
    if N >= 10:
        k = N // 10
        if k == 2:
            response.append('yi')
        elif k != 1:
            response.append(d[k])
        response.append("sip")
        N %= 10
    if N == 0:
        return " ".join(response)
    if N == 1:
        response.append("et")
    else:
        response.append(d[N])

    return " ".join(response)

exec(input().strip())
