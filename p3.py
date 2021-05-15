import struct


class C32:
    def __init__(self):
        self.activeState = 'A'

    def bolt(self):
        if self.activeState == 'A':
            self.activeState = 'B'
            return 0
        elif self.activeState == 'C':
            self.activeState = 'D'
            return 3
        elif self.activeState == 'E':
            self.activeState = 'G'
            return 9
        elif self.activeState == 'F':
            self.activeState = 'G'
            return 10
        else:
            return None

    def chip(self):
        if self.activeState == 'B':
            self.activeState = 'C'
            return 2
        elif self.activeState == 'C':
            self.activeState = 'H'
            return 5
        elif self.activeState == 'G':
            self.activeState = 'H'
            return 11
        else:
            return None

    def cull(self):
        if self.activeState == 'A':
            self.activeState = 'F'
            return 1
        elif self.activeState == 'D':
            self.activeState = 'E'
            return 7
        elif self.activeState == 'C':
            self.activeState = 'F'
            return 6
        elif self.activeState == 'E':
            self.activeState = 'F'
            return 8
        else:
            return None

    def skew(self):
        if self.activeState == 'C':
            self.activeState = 'E'
            return 4
        else:
            return None


# def create_massive_c(binary_data, value):
#     part = {
#         'C1': list(struct.unpack('=2b', binary_data[value:value + 2])),
#         'C2': struct.unpack('=f', binary_data[value + 2:value + 6])[0]
#     }
#     return part
#
#
# def create_massive_d(binary_data, value):
#     part = {
#         'D1': struct.unpack('=f', binary_data[value:value + 4])[0],
#         'D2': struct.unpack('= ', binary_data[value + 4:value + 12])[0],
#         'D3': list(struct.unpack('=2B', binary_data[value + 12:value + 14]))
#     }
#     return part
#
#
# def f31(binary_data):
#     structure = {}
#     a = 5
#     b1 = struct.unpack('=2H', binary_data[a + 0:a + 4])
#     c = list(struct.unpack('=' + 'H' * b1[0], binary_data[b1[1]:b1[1] + 2 * b1[0]]))
#     b1 = []
#     for value in c:
#         b1.append(create_massive_c(binary_data, value))
#
#     a = 3
#     b2 = struct.unpack('=q', binary_data[a + 6:a + 14])[0]
#     b3 = struct.unpack('=I', binary_data[a + 14:a + 18])[0]
#     b3 = create_massive_d(binary_data, b3)
#     b4 = struct.unpack('=H', binary_data[a + 18:a + 20])[0]
#     b5 = struct.unpack('=d', binary_data[a + 20:a + 28])[0]
#
#     a2 = struct.unpack('=q', binary_data[a + 28:a + 36])[0]
#     a3 = struct.unpack('=i', binary_data[a + 36:a + 40])[0]
#     a4 = struct.unpack('=B', binary_data[a + 40:a + 41])[0]
#     a5 = list(struct.unpack('=6B', binary_data[a + 41:a + 47]))
#
#     structure['A1'] = {
#         'B1': b1,
#         'B2': b2,
#         'B3': b3,
#         'B4': b4,
#         'B5': b5,
#     }
#     structure['A2'] = a2
#     structure['A3'] = a3
#     structure['A4'] = a4
#     structure['A5'] = a5
#
#     return structure
#
#
# print(f31((b'\x02ARMK\x03\x00D\x00%\x1b\xed\xb7\xc2\xfc&RJ\x00\x00\x00\t\xde\xc2'
#            b'\x84\xed\xed\xe0\xfd\xee\xbf\x16_\x9e\xd0\x84\xaf\x1a*\x1f\xd5\x1e\x01\x81'
#            b'XO\x95\x9ck\xc0\xa2*\x13\xb1\xca>\xeex\x07\x97t\xbfU,\x1cO\xa0>2\x008\x00'
#            b'>\x00\xd1\xf6\xbe=Q\xe2\xbb\xac\x92L\xd1\x91\xcf\xde')))
