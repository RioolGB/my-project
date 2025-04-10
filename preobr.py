"""Преобразование чисел в двоичную и восьмиричную системы"""
OCT = 8
BIN = 2
ZERO = 0

num: int = int(input('Введите число:\n'))
print(bin(num), oct(num), hex(num))
for div in BIN, OCT:
    new_num = num
    result: str = ''
    while new_num != ZERO:
        result = str(new_num % div) + result
        new_num //= div
    print(result)
