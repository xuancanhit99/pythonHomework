from p1 import f11, f12, f13, f14
from p2 import f21, f22, f23

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
print(f23([['vesucak32@rambler.ru', '26.04.99', None, 'Антон К. Вешучяк', 'Нет', 'Нет'], ['radmir46@mail.ru', '19.11.99', None, 'Радмир Т. Гитук', 'Да', 'Да'], ['ticazanz72@gmail.com', '16.07.00', None, 'Артем В. Тичазянц', 'Да', 'Да'], ['ticazanz72@gmail.com', '16.07.00', None, 'Артем В. Тичазянц', 'Да', 'Да'], ['tamman31@mail.ru', '19.06.03', None, 'Артур В. Тамман', 'Нет', 'Нет'] ]))
print(f23([['grigorij61@yahoo.com', '27.12.01', None, 'Григорий А. Телак', 'Нет', 'Нет'], ['timofej11@mail.ru', '23.01.01', None, 'Тимофей Р. Цушко', 'Да', 'Да'], ['ruslan82@mail.ru', '07.05.02', None, 'Руслан Ч. Бимев', 'Да', 'Да'], ['timofej11@mail.ru', '23.01.01', None, 'Тимофей Р. Цушко', 'Да', 'Да']]))