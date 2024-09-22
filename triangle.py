from math import cos, pi
a = int(input('Введите длину одной стороны '))
b = int(input('Введите длину второй стороны '))
d = int(input('Введите угол в градусах между этими сторонами '))
c = a ** 2 + b ** 2 - 2 * a * b * cos((d * pi) / 180)
print(c)