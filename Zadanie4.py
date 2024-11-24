a = int(input('Podaj wartość najmniejszą: '))
b = int(input('Podaj wartość największą: '))

parzyste = 0
nieparzyste = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f'Parzyste: {parzyste}\nNieparzyste: {nieparzyste}')