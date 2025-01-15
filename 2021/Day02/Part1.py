with open('input.gnumeric', 'r') as file:
    ins = [];
    for l in file.readlines():
        aux = l.strip().split(' ');
        ins.append([aux[0], int(aux[1])]);

    hor = 0;
    depth = 0;
    for i in ins:
        if i[0] == 'forward':
            hor += i[1];
        elif i[0] == 'up':
            depth -= i[1];
        else:
            depth += i[1];
    print(hor*depth);