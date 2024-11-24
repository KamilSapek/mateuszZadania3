a = int(input('Podaj wartość najmniejszą: '))
b = int(input('Podaj wartość największą: '))

for x in range(a, b):
    print(f'x = {x}   y = {x**2 + 1}')