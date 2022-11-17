'''
Napisz program, który przeanalizuje tabelę z wynikami poszczególnych rozgrywek zapisanych w
pliku scores.csv (1 linijka pliku = 1 rozgrywka).

Osoba z największą liczbą punktów wygrywa.

Punkty zdobywane za 1 rundę:
+3 pkt — za wygraną (najwięcej punktów) w danej rozgrywce
-1 pkt — za najgorszy wynik
0 pkt — w innych przypadkach
'''


import csv

def changeTypeToInt(value):
    if value == '':
        return 0
    return int(value)

darekScores = []
zdzisiekScores = []
edekScores = []

with open('scores.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:

        if row['Zdzisiek'].endswith('x'):
            tmp = row['Zdzisiek'][: -1]
            zdzisiek = changeTypeToInt(tmp)
            darek = changeTypeToInt(row['Darek'])
            edek = changeTypeToInt(row['Edek'])
            maxValue = max(zdzisiek, darek, edek)
            minValue = min(zdzisiek, darek, edek)
            print(maxValue, minValue)

        else:
            darek = changeTypeToInt(row['Darek'])
            edek = changeTypeToInt(row['Edek'])
            zdzisiek = changeTypeToInt(row['Zdzisiek'])
            maxValue = max(zdzisiek, darek, edek)
            minValue = min(zdzisiek, darek, edek)
            print(maxValue, minValue)




# print('Darek:\n',darekScores)
# print('Zdzisiek:\n',zdzisiekScores)
# print('Edek:\n',edekScores)

