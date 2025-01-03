def run(o, y):
    result = 0;
    if y == 'Y':
        result += 3;
    elif y == 'Z':
        result += 6;

    if (o == 'A' and y == 'Y') or (o == 'C' and y == 'Z') or (o == 'B' and y == 'X'):
        result += 1;
    elif (o == 'B' and y == 'Y') or (o == 'A' and y == 'Z') or (o == 'C' and y == 'X'):
        result += 2;
    else:
        result += 3;
    return result;

with open('input.gnumeric', 'r') as file:
    games = [];
    for g in file.readlines():
        games.append(g.strip().split(' '));

    sumg = 0;
    for g in games:
        sumg += run(g[0], g[1]);
    print(sumg);