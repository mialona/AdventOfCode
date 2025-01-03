def step(robot, move, map):
    if move == '^':
        wi = robot[0];
        for i in range(robot[0] - 1, -1, -1):
            if map[i][robot[1]] == '#':
                wi = i;
                break;
        ni = robot[0];
        for i in range(robot[0] - 1, wi, -1):
            if map[i][robot[1]] == '.':
                ni = i;
                break;
        if ni != robot[0]:
            for j in range(ni, robot[0], 1):
                map[j][robot[1]] = map[j + 1][robot[1]];
            map[robot[0]][robot[1]] = '.';
            robot[0] = robot[0] - 1;
    if move == 'v':
        wi = robot[0];
        for i in range(robot[0] + 1, len(map), 1):
            if map[i][robot[1]] == '#':
                wi = i;
                break;
        ni = robot[0];
        for i in range(robot[0] + 1, wi, 1):
            if map[i][robot[1]] == '.':
                ni = i;
                break;
        if ni != robot[0]:
            for j in range(ni, robot[0], -1):
                map[j][robot[1]] = map[j - 1][robot[1]];
            map[robot[0]][robot[1]] = '.';
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
                robot.append(line.find('@'));
            map.append(list(line));
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
            if map[i][j] == 'O':
                sum = sum + 100*i + j;
    print(sum);