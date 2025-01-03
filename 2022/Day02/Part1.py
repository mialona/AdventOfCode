def run(o, y):
    result = 0;
    if y == 'X':
        result += 1;
    elif y == 'Y':
        result += 2;
    else:
        result += 3;

    if (o == 'A' and y == 'X') or (o == 'B' and y == 'Y') or (o == 'C' and y == 'Z'):
        result += 3;
    elif (o == 'A' and y == 'Y') or (o == 'B' and y == 'Z') or (o == 'C' and y == 'X'):
        result += 6;
    return result;

with open('input.gnumeric', 'r') as file:
    games = [];
    for g in file.readlines():
        games.append(g.strip().split(' '));

    sumg = 0;
    for g in games:
        sumg += run(g[0], g[1]);
    print(sumg);