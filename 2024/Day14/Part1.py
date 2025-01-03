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
    ## printMap(maxX, maxY, robots);
    for i in range(100):
        step(maxX, maxY, robots);
    ## printMap(maxX, maxY, robots);

    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for robot in robots:
        if robot[0][0] < int(maxX/2) and robot[0][1] < int(maxY/2):
            sum1 = sum1 + 1;
        if robot[0][0] > int(maxX/2) and robot[0][1] < int(maxY/2):
            sum2 = sum2 + 1;
        if robot[0][0] < int(maxX/2) and robot[0][1] > int(maxY/2):
            sum3 = sum3 + 1;
        if robot[0][0] > int(maxX/2) and robot[0][1] > int(maxY/2):
            sum4 = sum4 + 1;
    print(sum1*sum2*sum3*sum4);