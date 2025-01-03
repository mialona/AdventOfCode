import copy;

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

    sum = 0;
    table[i][j] = '^';
    for k in range(len(table)):
        for l in range(len(table[k])):
            if table[k][l] == 'X':
                table2 = copy.deepcopy(table);
                table2[k][l] = '#';
                posx = i;
                posy = j;
                direction = 'N';

                list = []
                loop = False;
                while posx != -1 and posy != -1 and posx != len(table2) and posy != len(table2[0]) and not loop:
                    if direction == 'N':
                        if posx - 1 != -1 and table2[posx - 1][posy] == '#':
                            direction = 'E';
                            if [posx, posy, direction] in list:
                                loop = True;
                            else:
                                list.append([posx, posy, direction]);
                        else:
                            posx = posx - 1;
                    if direction == 'E':
                        if posy + 1 != len(table2[0]) and table2[posx][posy + 1] == '#':
                            direction = 'S';
                            if [posx, posy, direction] in list:
                                loop = True;
                            else:
                                list.append([posx, posy, direction]);
                        else:
                            posy = posy + 1;
                    if direction == 'S':
                        if posx + 1 != len(table2) and table2[posx + 1][posy] == '#':
                            direction = 'W';
                            if [posx, posy, direction] in list:
                                loop = True;
                            else:
                                list.append([posx, posy, direction]);
                        else:
                            posx = posx + 1;
                    if direction == 'W':
                        if posy - 1 != -1 and table2[posx][posy - 1] == '#':
                            direction = 'N';
                            if [posx, posy, direction] in list:
                                loop = True;
                            else:
                                list.append([posx, posy, direction]);
                        else:
                            posy = posy - 1;
                if loop:
                    sum = sum + 1;
    print(sum);