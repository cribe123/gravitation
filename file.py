G = 6.674e-11
m1 = float(input('Первый вес: '))
m2 = float(input('Второй вес: '))
r = float(input('Дистанция: '))
F = G * m1 * m2 / r**2
print(f'Сила: {F} ньютонов')
