import math


def f11(x, y, z):
    return y**4 - math.e**y - 95 + 27*(x**4 - math.cos(z))**2 + z**3 - (y**3 + 64*x**2 - 32)/(16*y**3 - x**8)


def f12(x):
    if x < 119:
        return x**5 - math.e**x - 95
    elif x < 141 & x >= 119:
        return (25*x**4 + (x**5)/67)**2 + x**8
    elif x < 161 & x >= 141:
        return math.cos(x**6 + x/84) + math.sin(x**8)
    elif x < 178 & x >= 161:
        return math.cos(38*x**8 - math.e**x) + math.log(math.e**x + math.sin(x) + 76)
    else:
        return 97*x + math.e**x


def f13(n, m):
    sum1 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            sum1 += math.tan(j) - math.tan(i)

    sum2 = 0
    for i in range(1, n+1):
        sum2 += math.e**i - 36*i**8 - 27

    return 45*sum1 + 92*sum2


def f14(n):
    if n == 0:
        return 7
    return math.cos(f14(n-1)) - math.tan(f14(n-1)) - 41
