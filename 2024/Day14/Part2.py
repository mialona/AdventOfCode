def step(maxX, maxY, robots):
    for robot in robots:
        robot[0][0] = (robot[0][0] + robot[1][0]) % maxX;
        robot[0][1] = (robot[0][1] + robot[1][1]) % maxY;

def printMap(maxX, maxY, robots):
    pos = [robot[0] for robot in robots];
    for j in range(maxY):
        for i in range(maxX):
            if [i, j] in pos:
                print(pos.count([i, j]), end='');
            else:
                print('.', end='');
        print();
    print();

with open('input.gnumeric', 'r') as file:
    robots = [];
    for line in file:
        robot = [];
        line = line.strip().split(' ');
        p = line[0][2:].split(',');
        robot.append([int(p[0]), int(p[1])]);
        v = line[1][2:].split(',');
        robot.append([int(v[0]), int(v[1])]);
        robots.append(robot);

    maxX = 101;
    maxY = 103;
    i = 0;
    while True:
        i = i + 1;
        step(maxX, maxY, robots);
        pos = [robot[0] for robot in robots];
        found = True;
        for p in pos:
            if pos.count(p) > 1:
                found = False;
        if found:
            break;

    printMap(maxX, maxY, robots);
    print(i)