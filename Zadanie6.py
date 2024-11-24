tekst = input('Podaj tekst: ')
litera = input('Podaj litere: ')

licznik = 0

for i in tekst:
    if i == litera:
        licznik += 1

print(licznik)