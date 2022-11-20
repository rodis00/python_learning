'''Napisz program do obliczania pola różnych figur płaskich.
W pliku figures.txt w podanym formacie zapisane są nazwy figur i odpowiednie dane,
potrzebne do obliczenia pola figury.
Napisz kod, który odczyta dane z pliku i automatycznie obliczy pola figur.
Następnie poszczególne pola figur wyświetli na ekranie.
Figury, dla których Twój kod powinien działać to:
- kwadrat
- trójkąt
- trapez
- koło.

Opcjonalnie:
Dodatkowo stwórz metodę, która poda statystyki przeliczonych figur:
- ile było poszczególnych rodzajów figur (np. 2 kwadraty, 4 koła itp)
- minimalna, maksymalna i średnia wartość pola poszczególnych rodzajów figur płaskich
(np. kwadrat — min. pole = 1, maks. pole = 64, śr. pole = 30,2 itp)

UWAGA: Załóż, że w pliku figures.txt mogą znaleźć się figury, których pola
program nie potrafi przeliczyć i obsłuż taką sytuację.'''


import math

def scores(figure, amount, field, dict):
    dict[figure]['amount'] += amount
    dict[figure]['fields'].append(field)
    maximum = max(dict[figure]['fields'])
    minimum = min(dict[figure]['fields'])
    tmp = 0
    for field in dict[figure]['fields']:
        tmp += field
    middle = tmp / len(dict[figure]['fields'])
    dict[figure]['max'] = maximum
    dict[figure]['min'] = minimum
    dict[figure]['middle'] = middle


with open('figures.txt', 'r') as file:
    dict = {
        'kwadrat':{
            'amount': 0,
            'fields': [],
            'max': 0,
            'min': 0,
            'middle': 0
        },
        'trojkat': {
            'amount': 0,
            'fields': [],
            'max': 0,
            'min': 0,
            'middle': 0
        },
        'trapez': {
            'amount': 0,
            'fields': [],
            'max': 0,
            'min': 0,
            'middle': 0
        },
        'kolo': {
            'amount': 0,
            'fields': [],
            'max': 0,
            'min': 0,
            'middle': 0
        }
    }
    for row in file:
        arr = row.split(',')
        if arr[0] == 'kwadrat':
            a = float(arr[1])
            field = a ** 2
            scores(arr[0], 1, field, dict)
            print('pole kwadratu =',field)
        elif arr[0] == 'trojkat':
            a = float(arr[1])
            h =float(arr[2])
            field = (a * h) / 2
            scores(arr[0], 1, field, dict)
            print('pole trojkata =',field)
        elif arr[0] == 'trapez':
            a = float(arr[1])
            b = float(arr[2])
            h = float(arr[3])
            field = ((a + b) * h) / 2
            scores(arr[0], 1, field, dict)
            print('pole trapezu =', field)
        elif arr[0] == 'kolo':
            r = float(arr[1])
            field = math.pi * (r ** 2)
            scores(arr[0], 1, field, dict)
            print('pole kola =', field)
        else:
            print('Nie obsluzono figury')

for key, value in dict.items():
    print(f"\n{key}:\nilosc: {value['amount']}\nmin.pole = {value['min']}"
          f"\nmax.pole = {value['max']}\nsr.pole = {value['middle']}")
