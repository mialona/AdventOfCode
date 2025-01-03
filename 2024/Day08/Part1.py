import copy;

with open('input.gnumeric', 'r') as file:
    table = [];
    for line in file:
        row = list(line.strip());
        table.append(row);

    sum = 0;
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] != '.':
                for k in range(len(table)):
                    for l in range(len(table[i])):
                        if i != k and j != l and table[i][j] == table[k][l] and i + 2*(k - i) > -1 and j + 2*(l - j) > -1 and i + 2*(k - i) < len(table) and j + 2*(l - j) < len(table[0]) and table[i + 2*(k - i)][j + 2*(l - j)] == '.':
                            sum = sum + 1;
    print(sum);