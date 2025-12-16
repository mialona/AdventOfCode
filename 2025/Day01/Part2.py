from math import floor, fmod;

def aux_floor(n, d):
    if n >= 0:
        return floor(n/d), n % d;
    else:
        return floor(-n/d) + 1, n % d;

with open('input.gnumeric', 'r') as file:
    list1 = [];
    for line in file:
        list1.append([line[0], int(line[1:])]);

    sum1 = 50;
    result = 0;
    for e in list1:
        if sum1 == 0 and e[0] == 'L':
            result -= 1;
        if e[0] == 'R':
            sum1 += e[1];
        else:
            sum1 -= e[1];
        aux1, aux2 = aux_floor(sum1, 100);
        if sum1 == 0:
            result += 1;
        result += aux1;
        sum1 = aux2;
    print(result);