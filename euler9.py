a = m^2 - n^2 , b = 2mn , c = m^2 + n^2 


def spt(sum):
    for m in range(sum):
        for n in range(m, sum):
            a = m ** 2 - n ** 2
            b = 2 * (m * n)
            c = m ** 2 + n ** 2
            if a + b + c == 1000:
                return (a,b,c,)