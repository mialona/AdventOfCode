def function(i, j, table, checked):
    area = 1;
    per = 0;
    checked.append([i, j]);
    # Case AAAB
    if table[i][j] == table[i + 1][j] and table[i][j] == table[i][j + 1] and table[i][j] != table[i + 1][j + 1]:
        per = per + 1;
    if table[i][j] == table[i - 1][j] and table[i][j] == table[i][j + 1] and table[i][j] != table[i - 1][j + 1]:
        per = per + 1;
    if table[i][j] == table[i + 1][j] and table[i][j] == table[i][j - 1] and table[i][j] != table[i + 1][j - 1]:
        per = per + 1;
    if table[i][j] == table[i - 1][j] and table[i][j] == table[i][j - 1] and table[i][j] != table[i - 1][j - 1]:
        per = per + 1;
    # Case ABBB
    if table[i][j] != table[i + 1][j] and table[i][j] != table[i][j + 1] and table[i][j] != table[i + 1][j + 1]:
        per = per + 1;
    if table[i][j] != table[i - 1][j] and table[i][j] != table[i][j + 1] and table[i][j] != table[i - 1][j + 1]:
        per = per + 1;
    if table[i][j] != table[i + 1][j] and table[i][j] != table[i][j - 1] and table[i][j] != table[i + 1][j - 1]:
        per = per + 1;
    if table[i][j] != table[i - 1][j] and table[i][j] != table[i][j - 1] and table[i][j] != table[i - 1][j - 1]:
        per = per + 1;
    # Case ABAB
    if table[i][j] != table[i + 1][j] and table[i][j] != table[i][j + 1] and table[i][j] == table[i + 1][j + 1]:
        per = per + 1;
    if table[i][j] != table[i - 1][j] and table[i][j] != table[i][j + 1] and table[i][j] == table[i - 1][j + 1]:
        per = per + 1;
    if table[i][j] != table[i + 1][j] and table[i][j] != table[i][j - 1] and table[i][j] == table[i + 1][j - 1]:
        per = per + 1;
    if table[i][j] != table[i - 1][j] and table[i][j] != table[i][j - 1] and table[i][j] == table[i - 1][j - 1]:
        per = per + 1;
    if not [i + 1, j] in checked and table[i][j] == table[i + 1][j]:
            a1, p1 = function(i + 1, j, table, checked);
            area = area + a1;
            per = per + p1;
    if not [i - 1, j] in checked and table[i][j] == table[i - 1][j]:
            a2, p2 = function(i - 1, j, table, checked);
            area = area + a2;
            per = per + p2;
    if not [i, j + 1] in checked and table[i][j] == table[i][j + 1]:
            a3, p3 = function(i, j + 1, table, checked);
            area = area + a3;
            per = per + p3;
    if not [i, j - 1] in checked and table[i][j] == table[i][j - 1]:
            a4, p4 = function(i, j - 1, table, checked);
            area = area + a4;
            per = per + p4;

    return area, per;

with open('input.gnumeric', 'r') as file:
    table = [];
    for line in file:
        row = list(line.strip());
        table.append(['.'] + row + ['.']);
    table.insert(0, len(table[0])*['.'])
    table.insert(len(table) + 1, len(table[0])*['.'])

    sum = 0;
    checked = []
    for i in range(1, len(table) - 1):
        for j in range(1, len(table[0]) - 1):
            if not [i, j] in checked:
                area, per = function(i, j, table, checked);
                sum = sum + area*per;
    print(sum);