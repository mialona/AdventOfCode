with open('input.gnumeric', 'r') as file:
    list1 = [];
    for line in file:
        list1.append([line[0], int(line[1:])]);

    sum1 = 50;
    result = 0;
    for e in list1:
        if e[0] == 'R':
            sum1 += e[1];
        else:
            sum1 -= e[1];
        if sum1 % 100 == 0:
            result += 1;
    print(result);