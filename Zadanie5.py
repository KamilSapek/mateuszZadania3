from random import randint

orzel = 0
reszka = 0

for i in range(int(input('Ile razy rzucic monetą?: '))):
    if randint(0, 1) == 0:
        orzel += 1
    else:
        reszka += 1

print(f'Orzeł: {orzel}\nReszka: {reszka}')