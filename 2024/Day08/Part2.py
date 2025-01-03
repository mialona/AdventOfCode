import copy;

with open('input.gnumeric', 'r') as file:
    table = [];
    for line in file:
        row = list(line.strip());
        table.append(row);

    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] != '.' and table[i][j] != '#':
                for k in range(len(table)):
                    for l in range(len(table[i])):
                        if i != k and j != l and table[i][j] == table[k][l]:
                            n = 2;
                            while i + n*(k - i) > -1 and j + n*(l - j) > -1 and i + n*(k - i) < len(table) and j + n*(l - j) < len(table[0]):
                                if table[i + n*(k - i)][j + n*(l - j)] == '.':
                                    table[i + n*(k - i)][j + n*(l - j)] = '#';
                                n = n + 1;

    f = open("Part2.output", "w")
    for line in table:
        f.write(''.join(line)+'\n');
    f.close()

    sum = 0;
    for line in table:
        sum = sum + len(line) - line.count('.');
    print(sum)