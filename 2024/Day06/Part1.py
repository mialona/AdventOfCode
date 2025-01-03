with open('input.gnumeric', 'r') as file:
    table = [];
    for line in file:
        row = list(line.strip());
        table.append(row);

    for i in range(len(table)):
        j = next((k for k in range(len(table[i])) if table[i][k] == '^'), -1);
        if j > -1:
            break;
    posx = i;
    posy = j;
    direction = 'N';

    while posx != -1 and posy != -1 and posx != len(table) and posy != len(table[0]):
        table[posx][posy] = 'X';
        if direction == 'N':
            if posx - 1 != -1 and table[posx - 1][posy] == '#':
                direction = 'E';
            else:
                posx = posx - 1;
        if direction == 'E':
            if posy + 1 != len(table[0]) and table[posx][posy + 1] == '#':
                direction = 'S';
            else:
                posy = posy + 1;
        if direction == 'S':
            if posx + 1 != len(table) and table[posx + 1][posy] == '#':
                direction = 'W';
            else:
                posx = posx + 1;
        if direction == 'W':
            if posy - 1 != -1 and table[posx][posy - 1] == '#':
                direction = 'N';
            else:
                posy = posy - 1;

    f = open("Part1.output", "w")
    for line in table:
        f.write(''.join(line)+'\n');
    f.close()

    sum = 0;
    for x in table:
        sum = sum + x.count('X');
    print(sum);