from p1 import f11, f12, f13, f14
from p2 import f21, f22

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