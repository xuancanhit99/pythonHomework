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


D_SIZE = 4 + 2 + 2
C_SIZE = 1 + 4 + D_SIZE + 2
B_SIZE = 4 + 2 + 1
A_SIZE = 2 + 8 + 4 * 6 + 8 + 4 + 4 + 4 + 2 + 4 + 4


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset: offset + D_SIZE]
    d_parsed = struct.unpack('<iHH', d_bytes)
    d2_bytes = byte_string[d_parsed[2]:d_parsed[2] + d_parsed[1] * 8]
    d2_parsed = struct.unpack('<' + 'Q' * d_parsed[1], d2_bytes)
    return {'D1': d_parsed[0],
            'D2': list(d2_parsed)}


def parse_c(offset, byte_string):
    c12_bytes = byte_string[offset: offset + 5]
    c12_parsed = struct.unpack('<bI', c12_bytes)
    c3_parsed = parse_d(offset + 5, byte_string)
    c4_bytes = byte_string[offset + 5 + D_SIZE:offset + 5 + D_SIZE + 2]
    c4_parsed = struct.unpack('<' + 'H', c4_bytes)
    return {'C1': c12_parsed[0],
            'C2': c12_parsed[1],
            'C3': c3_parsed,
            'C4': c4_parsed[0]}


def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('<fhB', b_bytes)
    return {'B1': b_parsed[0],
            'B2': b_parsed[1],
            'B3': b_parsed[2]}


def parse_a(offset, byte_string):
    a123_byte = byte_string[offset:offset + 34]
    a123_parsed = struct.unpack('<hqffffff', a123_byte)
    a4_byte = byte_string[offset + 34:offset + 34 + 8]
    a4_parsed = struct.unpack('<' + 'd', a4_byte)
    a5_bytes = byte_string[offset + 42:offset + 42 + 4 + 4]
    a5_parsed = struct.unpack('<II', a5_bytes)
    a5_bytes_address = byte_string[a5_parsed[1]:a5_parsed[1] + a5_parsed[0] * 2]
    a5_parsed_address = struct.unpack('<' + 'H' * a5_parsed[0], a5_bytes_address)
    a5_list = [parse_b(addr, byte_string) for addr in a5_parsed_address]
    a6_bytes = byte_string[offset + 2 + 8 + 4 * 6 + 8 + 4 + 4: offset + 2 + 8 + 4 * 6 + 8 + 4 + 4 + 4]
    a6_parsed = struct.unpack('<' + 'I', a6_bytes)
    a7_bytes = byte_string[offset + 2 + 8 + 4 * 6 + 8 + 4 + 4 + 4: offset + 2 + 8 + 4 * 6 + 8 + 4 + 4 + 4 + 2]
    a7_parsed = struct.unpack('<h', a7_bytes)
    a8_bytes = byte_string[offset + 2 + 8 + 4 * 6 + 8 + 4 + 4 + 4 + 2: offset + A_SIZE]
    a8_parsed = struct.unpack('<II', a8_bytes)
    a8_bytes_address = byte_string[a8_parsed[1]:a8_parsed[1] + a8_parsed[0] * 2]
    a8_parsed_address = struct.unpack('<' + 'h' * a8_parsed[0], a8_bytes_address)
    return {
        'A1': a123_parsed[0],
        'A2': a123_parsed[1],
        'A3': list(a123_parsed[2:8]),
        'A4': a4_parsed[0],
        'A5': a5_list,
        'A6': parse_c(a6_parsed[0], byte_string),
        'A7': a7_parsed[0],
        'A8': list(a8_parsed_address)
    }


def f31(byte_string):
    return parse_a(4, byte_string)
