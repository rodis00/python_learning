'''
Magiczne kwadraty
Napisz program, który sprawdzi, czy podany w pliku tekstowym kwadrat, jest kwadratem magicznym.
To znaczy czy w każdej kolumnie, wierszu i po obu przekątnych suma wartości jest taka sama.
Załóż, że w podanym pliku tekstowym znajduje się tylko 1 magiczny kwadrat.
Dodatkowo niech program sprawdzi czy wszystkie wartości w kwadracie są unikalne.
'''


with open('magic_square_3.txt', 'r') as file:
    arr = []
    for row in file:
        list = []
        tmp = row.split()
        for el in tmp:
            if el.endswith(','):
                el = el[:-1]
                list.append(int(el))
            else:
                list.append(int(el))
        arr.append(list)


columns = []
rows = []
diagonal1 = 0
diagonal2 = 0

for row in range(len(arr)):
    sum = 0
    for col in arr:
        sum += col[row]
    columns.append(sum)

for item in arr:
    sum = 0
    for row in item:
        sum += row
    rows.append(sum)


index_i = 0
index_j = len(arr) - 1
for i in range(len(arr)):
    diagonal1 += arr[index_i][index_i]
    diagonal2 += arr[index_i][index_j]
    index_i += 1
    index_j -= 1


print(rows)
print(columns)
print(diagonal1)
print(diagonal2)

isMagic = False
if diagonal1 == diagonal2:
    for list in rows, columns:
        for item in list:
            if item == diagonal2:
                isMagic = True
            else:
                isMagic = False
                break

# sprawdzenie unikalności liczb w tablicy
newArr = []
for row in arr:
    for item in row:
        if item not in newArr:
            newArr.append(item)

if len(newArr) % len(arr) != 0:
    isMagic = False


print("jest magiczny" if isMagic else "nie jest magiczny")