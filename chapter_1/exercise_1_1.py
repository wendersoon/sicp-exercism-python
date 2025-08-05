print(10)
print(5 + 3 + 4)
print(9 - 1)
print(6 / 2)
print((2 * 4) + (4 - 6))
a = 3
b = a + 1
print(a + b + (a * b))
print(a == b)

if ((b > a) and (b < (a * b))):
    print(b)
else:
    print(a)

if (a == 4):
    print(6)
elif (b == 4):
    print(6 + 7 + a)
else:
    print(25)

print(2 + b if b > a else a)

print((a + 1) * (a if a > b else b if a < b else -1))