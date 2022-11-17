# zad 1
'''Napisz metodę, która sprawdzi, czy podana wartość val znajduje
się w liście liczb digits. Szkielet funkcji znajdziesz poniżej.'''


from random import randint, choice
from typing import List


def f(val: int, digits: List[int]) -> bool:
    return val in digits



n = 10 # Liczba elementów do wylosowania
digits_example = [randint(-1000, 1000) for _ in range(n)]

val = choice(digits_example)
print(f(5, digits_example))


# zad 2
'''
Użytkownik podaje liczbę w zakresie od 101 - 99999.
Napisz program, który zamieni kolejnością cyfry w podanej liczbie.

Przykład

365 -> 563
90238 -> 83209
'''

print('Podaj swoją liczbę w zakresie (101 - 99999)')
userInput = input('-> ')
while True:
    if int(userInput) < 101 or int(userInput) > 99999:
        print('Poprawny zakres to (101 - 99999)')
        userInput = input('-> ')
    else:
        convertInput = userInput[::-1]
        print(f'{userInput} -> {convertInput}')
        break

