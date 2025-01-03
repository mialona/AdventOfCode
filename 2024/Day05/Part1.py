with open('input.gnumeric', 'r') as file:
    lines = [line.rstrip() for line in file]

    i = 0;
    rules = [];
    while lines[i] != '':
        rules.append(lines[i].strip().split('|'));
        i = i + 1;
    i = i + 1;
    updates = [];
    while i < len(lines):
        updates.append(lines[i].strip().split(','));
        i = i + 1;

    sum = 0;
    for i in range(len(updates)):
        correctly = True;
        for j in range(len(updates[i])):
            if correctly:
                for k in range(j + 1, len(updates[i])):
                    if [updates[i][k], updates[i][j]] in rules:
                        correctly = False;
                        break;
        if correctly:
            sum = sum + int(updates[i][int(len(updates[i])/2)])
    print(sum);