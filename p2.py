
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


def f23(input):
    column = []
    for row in input:
        column.append(row[0])


    print(len(input))
    print(input)
    return 1


f23([['vesucak32[at]rambler.ru', '26.04.99', ' ', 'Антон К. Вешучяк', 'Нет', 'Нет'], ['radmir46[at]mail.ru', '19.11.99', ' ', 'Радмир Т. Гитук', 'Да', 'Да'], ['ticazanz72[at]gmail.com', '16.07.00', ' ', 'Артем В. Тичазянц', 'Да', 'Да'], ['ticazanz72[at]gmail.com', '16.07.00', ' ', 'Артем В. Тичазянц', 'Да', 'Да'], ['tamman31[at]mail.ru', '19.06.03', ' ', 'Артур В. Тамман', 'Нет', 'Нет'] ])

