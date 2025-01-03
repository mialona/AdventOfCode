import copy;

def search(n, x, y, table, lnines):
    if table[x][y] == '9':
        lnines.append([x, y]);
    else:
        if x + 1 < len(table) and int(table[x + 1][y]) == n + 1:
            search(n + 1, x + 1, y, table, lnines);
        if x - 1 >= 0 and int(table[x - 1][y]) == n + 1:
            search(n + 1, x - 1, y, table, lnines);
        if y + 1 < len(table[0]) and int(table[x][y + 1]) == n + 1:
            search(n + 1, x, y + 1, table, lnines);
        if y - 1 >= 0 and int(table[x][y - 1]) == n + 1:
            search(n + 1, x, y - 1, table, lnines);

with open('input.gnumeric', 'r') as file:
    table = [];
    for line in file:
        row = list(line.strip());
        table.append(row);

    sum = 0;
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == '0':
                lnines = [];
                search(0, i, j, table, lnines);
                sum = sum + len(lnines);
    print(sum);