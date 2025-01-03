def fUp(x, y, map, listb):
    if not [x,y] in listb:
        listb.append([x,y]);
        if map[x - 1][y] == '.':
            return True;
        if map[x - 1][y] == '[':
            return fUp(x - 1, y, map, listb) and fUp(x - 1, y + 1, map, listb);
        if map[x - 1][y] == ']':
            return fUp(x - 1, y, map, listb) and fUp(x - 1, y - 1, map, listb);
        return False;
    else:
        return True;

def fDown(x, y, map, listb):
    if not [x,y] in listb:
        listb.append([x,y]);
        if map[x + 1][y] == '.':
            return True;
        if map[x + 1][y] == '[':
            return fDown(x + 1, y, map, listb) and fDown(x + 1, y + 1, map, listb);
        if map[x + 1][y] == ']':
            return fDown(x + 1, y, map, listb) and fDown(x + 1, y - 1, map, listb);
        return False;
    else:
        return True;

def step(robot, move, map):
    if move == '^':
        listb = [];
        posible = fUp(robot[0], robot[1], map, listb);
        listb.sort(key = lambda element: element[0]);
        if posible:
            for b in listb:
                map[b[0] - 1][b[1]] = map[b[0]][b[1]];
                map[b[0]][b[1]] = '.';
            robot[0] = robot[0] - 1;
    if move == 'v':
        listb = [];
        posible = fDown(robot[0], robot[1], map, listb);
        listb.sort(key = lambda element: element[0], reverse = True);
        if posible:
            for b in listb:
                map[b[0] + 1][b[1]] = map[b[0]][b[1]];
                map[b[0]][b[1]] = '.';
            robot[0] = robot[0] + 1;
    if move == '<':
        wi = robot[1];
        for i in range(robot[1] - 1, -1, -1):
            if map[robot[0]][i] == '#':
                wi = i;
                break;
        ni = robot[1];
        for i in range(robot[1] - 1, wi, -1):
            if map[robot[0]][i] == '.':
                ni = i;
                break;
        if ni != robot[1]:
            for j in range(ni, robot[1], 1):
                map[robot[0]][j] = map[robot[0]][j + 1];
            map[robot[0]][robot[1]] = '.';
            robot[1] = robot[1] - 1;
    if move == '>':
        wi = robot[1];
        for i in range(robot[1] + 1, len(map[0]), 1):
            if map[robot[0]][i] == '#':
                wi = i;
                break;
        ni = robot[1];
        for i in range(robot[1] + 1, wi, 1):
            if map[robot[0]][i] == '.':
                ni = i;
                break;
        if ni != robot[1]:
            for j in range(ni, robot[1], -1):
                map[robot[0]][j] = map[robot[0]][j - 1];
            map[robot[0]][robot[1]] = '.';
            robot[1] = robot[1] + 1;

def printMap(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            print(map[i][j], end='');
        print();
    print();

with open('input.gnumeric', 'r') as file:
    i = 0;
    map = [];
    robot = [];
    lines = file.readlines();
    while True:
        line = lines[i].strip();
        if len(line) > 0:
            if line.find('@') > -1:
                robot.append(i);
                robot.append(2*line.find('@'));
            row = [];
            for p in list(line):
                if p == '#':
                    row.append('#');
                    row.append('#');
                if p == 'O':
                    row.append('[');
                    row.append(']');
                if p == '.':
                    row.append('.');
                    row.append('.');
                if p == '@':
                    row.append('@');
                    row.append('.');
            map.append(row);
        else:
            break;
        i = i + 1;

    i = i + 1;
    moves = [];
    while i < len(lines):
        moves = moves + list(lines[i].strip());
        i = i + 1;

    for move in moves:
        step(robot, move, map);
    printMap(map);

    sum = 0;
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '[':
                sum = sum + 100*i + j;
    print(sum);