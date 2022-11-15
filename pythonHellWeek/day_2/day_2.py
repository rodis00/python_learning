'''
Zadanie 1.
Z pliku tekstowego wypisz w konsoli, tylko linie ze słowem Python.

Zadanie 2.
Z pliku tekstowego wypisz w konsoli, słowa rozpoczynające się na literę podaną przez użytkownika.
'''

# zad 1
with open('content.txt', 'r') as file:
    for line in file:
        for word in line.split(' '):
            if word.endswith('\n'):
                word = word[: -2]
            if word.endswith('.'):
                word = word[: -1]
            if word == 'Python':
                print(line, end='')


# zad 2
userLetter = input('\n\nPodaj swoją literę: ')

with open('content.txt', 'r') as file:
    for line in file:
        for word in line.split(' '):
            if word.startswith(userLetter.lower()) or word.startswith(userLetter.upper()):
                if word.endswith('\n'):
                    print(word[: -2], end=' ')
                elif word.endswith('.'):
                    print(word[: -1], end=' ')
                else:
                    print(word, end=' ')
    print()

