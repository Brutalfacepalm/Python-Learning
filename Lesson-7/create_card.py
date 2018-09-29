import random

def fill(rows, cols):
    numbers, card = [], []
    # создадим вложенные списки с 3 уникальными числами для каждого столбца карточки
    # в зависимости от разряда стобца
    for c in range(cols):
        if c == 0:
            numbers.append(random.sample(range(1,9),5))
        elif c == cols - 1:
            numbers.append(random.sample(range(c * 10, (c + 1) * 10), 5))
        else:
            numbers.append(random.sample(range(c * 10, c * 10 + 9), 5))

    for r in range(rows):
        card.append([])
        # создадим последовательность из 5-и номеров непустых ячеек для каждой строчки карточки
        row = random.sample(range(1,10),5)
        # rows = [i for i in range(1, 10)]
        # for rs in rows:
        #     if not rs in row:
        #         rows[rows.index(rs)] = ' '
        # print(rows)



        for c in range(1, 10):
            if c in row:
                card[r].append(numbers[c - 1][r]) # заполняем непустую ячейку числом
            else:
                card[r].append(' ')
        # row.clear()
    return card