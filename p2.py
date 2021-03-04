
def f21(x):
    if x[3] == 'e':
        if x[2] == 1997:
            if x[1] == 'pic':
                return 0
            elif x[1] == 'text':
                return 1
            elif x[1] == 'tex':
                return 2
        elif x[2] == 1961:
            if x[1] == 'pic':
                return 3
            elif x[1] == 'text':
                return 4
            elif x[1] == 'tex':
                return 5
    elif x[3] == 'asn.1':
        if x[0] == 'apex':
            return 6
        elif x[0] == 'css':
            return 7
        elif x[0] == 'pod':
            if x[1] == 'pic':
                return 8
            elif x[1] == 'text':
                return 9
            elif x[1] == 'tex':
                return 10


def f22(a):
    f = int(a) >> 30
    e = (int(a) >> 23) & 0b001111111
    d = (int(a) >> 21) & 0b00000000011
    c = (int(a) >> 18) & 0b00000000000111
    b = (int(a) >> 14) & 0b000000000000001111
    an = int(a) & 0b00000000000000000011111111111111

    x = (b << 28) + (d << 26) + (c << 23) + (e << 16) + (f << 14) + an
    return x


def cm(a, b):
    result = True

    for i in range(len(a)):
        if a[i] != b[i]:
            result = False
            break
    return result


def f23(a):
    b = []
    for i in range(len(a)):
        b.append([])
        for j in range(len(a[i])):
            if a[i][j] is not None:
                b[i].append(a[i][j])

    c = []
    for i in range(len(b)):
        c.append([])
        for j in range(len(b[i])):
            if j == 0:
                c[i].append(b[i][j])
            else:
                if b[i][j] != c[i][j-1]:
                    c[i].append(b[i][j])

    d = []
    d.append(c[0])
    for i in range(1, len(c)):
        check = False
        for j in range(len(d)):
            if cm(c[i], d[j]):
                check = True
        if not check:
            d.append(c[i])

    for i in range(len(d)):
        for j in range(len(d[i])):
            if '@' in d[i][j]:
                d[i][j] = d[i][j].replace('@', '[at]')
            elif d[i][j].count('.') == 2 and ' ' not in d[i][j]:
                lst = d[i][j].split('.')
                lst.reverse()
                d[i][j] = '/'.join(lst)
            elif d[i][j].count(' ') == 2 and d[i][j].count('.') == 1:
                ind = d[i][j].index('.')
                d[i][j] = d[i][j][:ind-2] + d[i][j][ind+1:]
                lst = d[i][j].split(' ')
                lst.reverse()
                d[i][j] = ' '.join(lst)
            elif d[i][j] == 'Нет':
                d[i][j] = 'Не выполнено'
            elif d[i][j] == 'Да':
                d[i][j] = 'Выполнено'
    return d
