import pprint
from p1 import f11, f12, f13, f14
from p2 import f21, f22, f23
from p3 import f31

print("Task 1.1")
print("f(-10,18,34) = " + "%.2e" % f11(-10, 18, 34))
print("f(59,56,-23) = " + "%.2e" % f11(59, 56, -23))

print("\nTask 1.2")
print("f(181) = " + "%.2e" % f12(181))
print("f(64) = " + "%.2e" % f12(64))

print("\nTask 1.3")
print("f(81,39) = " + "%.2e" % f13(81, 39))
print("f(20,100) = " + "%.2e" % f13(20, 100))

print("\nTask 1.4")
print("f(12) = " + "%.2e" % f14(12))
print("f(16) = " + "%.2e" % f14(16))

print("\nTask 2.1")
print(f21(['apex', 'pic', 1997, 'e']))
print(f21(['pod', 'text', 1961, 'e']))

print("\nTask 2.2")
print(hex(f22(0x80c58478)))
print(hex(f22(0xbcdcdf7d)))

print("\nTask 2.3")
print(f23([['vesucak32@rambler.ru', '26.04.99', None, 'Антон К. Вешучяк', 'Нет', 'Нет'],
           ['radmir46@mail.ru', '19.11.99', None, 'Радмир Т. Гитук', 'Да', 'Да'],
           ['ticazanz72@gmail.com', '16.07.00', None, 'Артем В. Тичазянц', 'Да', 'Да'],
           ['ticazanz72@gmail.com', '16.07.00', None, 'Артем В. Тичазянц', 'Да', 'Да'],
           ['tamman31@mail.ru', '19.06.03', None, 'Артур В. Тамман', 'Нет', 'Нет']]))
print(f23([['grigorij61@yahoo.com', '27.12.01', None, 'Григорий А. Телак', 'Нет', 'Нет'],
           ['timofej11@mail.ru', '23.01.01', None, 'Тимофей Р. Цушко', 'Да', 'Да'],
           ['ruslan82@mail.ru', '07.05.02', None, 'Руслан Ч. Бимев', 'Да', 'Да'],
           ['timofej11@mail.ru', '23.01.01', None, 'Тимофей Р. Цушко', 'Да', 'Да']]))

print("\nTask 3.1")
pprint.pprint(f31(b'\x06PUU\xd9rh\xa2\x9b\\\xf2O\x9f\xfd\xab\xb2|?Sm\xaf>\x96\x03!\xbf\xedP'
                  b'\x9f\xbdL|H\xbe\xa2\xdb]?\x98x\xac\xb6\xc5u\xd1?\x03\x00\x00\x00Y\x00'
                  b'\x00\x00o\x00\x00\x00\x0e\xa1\x04\x00\x00\x00~\x00\x00\x00}:\xc4>'
                  b'\xcc\xfdb\xd1\x9a\xae>\x07\x05\x11\x88\x00G?b\xc7\x87D\x00K\x00R\x00\x9c'
                  b'\x97{u:\xcd_\x10?\xddL\xa4\xaf\xd6\xa0\x8f}\xcf9\x87\xfb^\x8f\x1a\x8b'
                  b'\x02\x00_\x00W\x17\x83&KM\x9c\xbb\xf56'))

pprint.pprint(f31(b'\x06PUU\xe3\xce\x17\xc8\xdd\xe7E\xb6n\x85I\xddl>%/e\xbf\xbf\x10Q=^\xd0'
                  b'8?\xb7\xceC\xbf.k\xaf=\xd0\xdb\x98\xd4\xa2d\xdb?\x03\x00\x00\x00Y\x00'
                  b'\x00\x00o\x00\x00\x00\x11\x1a\x04\x00\x00\x00~\x00\x00\x00\x08\x8ca?*t\xdcZ'
                  b'3\x9b=\x84\xb9\xdd4\xf4X\xbfH\xb3nD\x00K\x00R\x00\x929"\xc2NY\xa4Rr'
                  b'\xba\xcfZ\x18\x12i\x19P\x0c\\\x82\xa6A\xff\x06\xa6\x02\x00_\x00D@$\xf5'
                  b'\x85\x01\x94\xaa\xf40'))
