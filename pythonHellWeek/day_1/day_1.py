'''
Gra w zgadywanie

System losuje liczbę całkowitą z przedziału 1 do 256.
Następnie prosi użytkownika o zgadnięcie liczby.
Po każdorazowym wpisaniu liczby przez gracza system pokazuje informację:
- "za mało", gdy podana liczba jest za niska
- "za dużo", gdy podana liczba jest za wysoka

Runda kończy się, gdy użytkownik poda poprawną liczbę.
Użytkownik powinien mieć możliwość wyboru, czy chce zagrać jeszcze raz.
'''
import random

play = True
while play:
    number = random.randint(1, 256)
    print('Gra w zgadywanie:')
    playerNumber = int(input('Podaj swoją liczbę: '))
    while True:
        if playerNumber > number:
            print('za dużo')
            playerNumber = int(input('Podaj swoją liczbę: '))
        elif playerNumber < number:
            print('za mało')
            playerNumber = int(input('Podaj swoją liczbę: '))
        else:
            print('zgadłeś!!! Chcesz zagrać jeszcze raz? (y/n)')
            answer = input('-> ').lower()
            if answer == 'n':
                play = False
                break
            else:
                break

