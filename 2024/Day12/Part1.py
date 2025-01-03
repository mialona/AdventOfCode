def function(i, j, table, checked):
    area = 1;
    per = 0;
    checked.append([i, j]);
    if not [i + 1, j] in checked or table[i][j] != table[i + 1][j]:
        if i + 1 < len(table) and table[i][j] == table[i + 1][j]:
            a1, p1 = function(i + 1, j, table, checked);
            area = area + a1;
            per = per + p1;
        else:
            per = per + 1;
    if not [i - 1, j] in checked or table[i][j] != table[i - 1][j]:
        if i - 1 >= 0 and table[i][j] == table[i - 1][j]:
            a2, p2 = function(i - 1, j, table, checked);
            area = area + a2;
            per = per + p2;
        else:
            per = per + 1;
    if not [i, j + 1] in checked or table[i][j] != table[i][j + 1]:
        if j + 1 < len(table[0]) and table[i][j] == table[i][j + 1]:
            a3, p3 = function(i, j + 1, table, checked);
            area = area + a3;
            per = per + p3;
        else:
            per = per + 1;
    if not [i, j - 1] in checked or table[i][j] != table[i][j - 1]:
        if j - 1 >= 0 and table[i][j] == table[i][j - 1]:
            a4, p4 = function(i, j - 1, table, checked);
            area = area + a4;
            per = per + p4;
        else:
            per = per + 1;

    return area, per;

with open('input.gnumeric', 'r') as file:
    table = [];
    for line in file:
        row = list(line.strip());
        table.append(row);

    sum = 0;
    checked = []
    for i in range(len(table)):
        for j in range(len(table[0])):
            if not [i, j] in checked:
                area, per = function(i, j, table, checked);
                sum = sum + area*per;
    print(sum);