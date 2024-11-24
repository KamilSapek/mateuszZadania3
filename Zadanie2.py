x = int(input('Podaj wartość największą: '))
y = int(input('Podaj wartość najmniejszą: '))
for i in range(x, y, -1):
    if i != y + 1:
        print(i, end=', ')
    else:
        print(i, end='.')