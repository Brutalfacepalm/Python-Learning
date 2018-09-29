import random

def fill(rows, cols):
    row, numbers, card = set(), [], []
    # создадим вложенные списки с 3 уникальными числами для каждого столбца карточки
    # в зависимости от разряда стобца
    for c in range(cols):
        if c == 0:
            while len(row) < rows:
                row.add(random.randint(1 , 9))
            numbers.append(list(row))
            row.clear()
        elif c == cols - 1:
            while len(row) < rows:
                row.add(random.randint(c * 10, (c + 1) * 10))
            numbers.append(list(row))
            row.clear()
        else:
            while len(row) < rows:
                row.add(random.randint(c * 10, c * 10 + 9))
            numbers.append(list(row))
            row.clear()

    for r in range(rows):
        card.append([])
        # создадим последовательность из 5-и номеров непустых ячеек для каждой строчки карточки
        while len(row) < 5:
            row.add(random.randint(1, 9))
        # для каждой строки карточки: при обнаружении непустой ячейки обратиться к списку чисел
        # и взять элемент подходящий по разряду(с-1) и номеру строки(r)
        for c in range(1, 10):
            if c in row:
                card[r].append(numbers[c - 1][r]) # заполняем непустую ячейку числом
            else:
                card[r].append(' ')
        row.clear()
    return card