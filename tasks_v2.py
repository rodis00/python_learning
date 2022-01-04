import random


def czy_ok1(password):
    is_ok = 0
    if len(password) == 8:
        is_ok = 1
    for letter in password:
        if letter.isdigit():
            is_ok = 1
        else:
            is_ok = 0
            break
    for i in range(len(password)-1):
        if password[i] == password[i + 1]:
            is_ok = 0
    return is_ok


def czy_ok2(password):
    is_ok = 0
    if 8 < len(password) < 10:
        is_ok = 1
    else:
        return 0
    if password[0].isupper() & password[len(password)-1].isupper():
        is_ok = 1
    else:
        is_ok = 0
    return is_ok


def dzielniki(number):
    ile = 0
    for i in range(1, number + 1):
        if number % i == 0:
            ile += 1
    return ile


def ostatnie(napis, n):
    new_napis = ""
    dlugosc = len(napis) - n
    for i in range(dlugosc, len(napis)):
        new_napis += napis[i]
    print(new_napis)


def zamiana2(tab, rozmiar):
    for i in range(rozmiar):
        if tab[i] % 2 == 0:
            tab[i] = 0
        else:
            tab[i] = 1


def ile_spacji(napis):
    ile = 0
    for letter in napis:
        if letter == ' ':
            ile += 1
    return ile


def zamiana(napis):
    ile = 0
    for letter in napis:
        if letter == ' ':
            napis[letter] = '_'
            ile += 1
    return ile


def suma(tab, rozmiar, liczba):
    suma = 0
    for number in tab:
        if number > liczba:
            suma += number
    return suma


def sumaMaxMin(tab, rozmiar):
    min = tab[0]
    max = tab[0]
    for i in range(rozmiar):
        if tab[i] > max:
            max = tab[i]
        if tab[i] < min:
            min = tab[i]
    suma = min + max
    return suma


def minParzysta(tab, rozmiar):
    min = 0
    for i in range(rozmiar):
        if tab[i] % 2 == 0:
            min = tab[i]
            break
    for i in range(rozmiar):
        if tab[i] % 2 == 0 & tab[i] < min:
            min = tab[i]
    return min


def czyNrRej(napis):
    is_ok = 0
    if napis[0].isupper() & napis[1].isupper():
        is_ok = 1
    else:
        return 0
    for letter in range(3, 8):
        if napis[letter].isdigit():
            is_ok = 1
        else:
            is_ok = 0
            break
    return is_ok


def f1(word):
    li = []
    for i in range(len(word)):
        for letter in word:
            if letter not in li:
                li.append(letter)

    return len(li)


def f2(napis):
    print("przed zamiana:")
    print(napis)
    print("po zamianie:")
    new_napis = ""
    for letter in napis:
        if letter.isalpha():
            new_napis += letter
        else:
            letter = '_'
            new_napis += letter
    print(new_napis)


def takieSame(tab_1, tab_2, rozmiar):
    new_tab = []
    for i in range(rozmiar):
        if tab_1[i] not in tab_2:
            if tab_1[i] not in new_tab:
                new_tab.append(tab_1[i])
                print(tab_1[i], end=", ")


print("zad_1: ", czy_ok1("01238771"))
print("zad_2: ", czy_ok2("PassworrD"))
print("zad_3: ", dzielniki(10))
print("zad_4: ", end="")
ostatnie("kowalski", 3)
print("zad_5\nprzed zamiana")
tab = [3, 24, 7, 4, 9, 10, 8]
print(tab)
print("po zamianie")
zamiana2(tab, 7)
print(tab)
print("zad_6: ", ile_spacji("Ala ma kota a kot ma Ale"))
print("zad_7: ", zamiana("Ala ma kota"))
print("zad_8: ", suma([1, 2, 3, 4, 5], 5, 3))
print("zad_9: ", sumaMaxMin([3, 5, 8, 1, 9, 2, 7], 7))
print("zad_10: ", minParzysta([3, 5, 8, 1, 9, 4, 7], 7))
print("zad_11: ", czyNrRej("LU 55555"))
print("zad_12: ", f1("Ala ma kota"))
print("zad_13: ")
f2("alo98.wTY8%p")
tab_1 = [random.randint(0, 10)for x in range(7)]
tab_2 = [random.randint(0, 10)for y in range(7)]
print(tab_1)
print(tab_2)
print("zad_14: ")
takieSame(tab_1, tab_2, 7)
