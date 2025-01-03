from functools import cache;

@cache
def function(nA, nB, x, y, mAx, mAy, mBx, mBy, mPx, mPy):
    if nA > 0 and nB > 0 and x <= mPx and y <= mPy:
        if x == mPx and y == mPy:
            return 3*(100 - nA) + (100 - nB);
        else:
            resultA = function(nA - 1, nB, x + mAx, y + mAy, mAx, mAy, mBx, mBy, mPx, mPy);
            resultB = function(nA, nB - 1, x + mBx, y + mBy, mAx, mAy, mBx, mBy, mPx, mPy);
            return min(resultA, resultB);
    else:
        return 500;

    return area, per;

with open('input.gnumeric', 'r') as file:
    i = 0;
    data = [];
    lines = file.readlines();
    while i < len(lines):
        machine = [];
        line = lines[i].strip();
        machine.append([int(line[line.find('X+') + 2 : line.find(',')]), int(line[line.find('Y+') + 2 :])]);
        line = lines[i + 1].strip();
        machine.append([int(line[line.find('X+') + 2 : line.find(',')]), int(line[line.find('Y+') + 2 :])]);
        line = lines[i + 2].strip();
        machine.append([int(line[line.find('X=') + 2 : line.find(',')]), int(line[line.find('Y=') + 2 :])]);
        i = i + 4;
        data.append(machine);

    sum = 0;
    for machine in data:
        result = function(100, 100, 0, 0, machine[0][0], machine[0][1], machine[1][0], machine[1][1], machine[2][0], machine[2][1]);
        if result <= 400:
            sum = sum + result;
    print(sum);