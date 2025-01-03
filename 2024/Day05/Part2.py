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
        j = 0;
        correctly = True;
        while j < len(updates[i]):
            for k in range(j + 1, len(updates[i])):
                if [updates[i][k], updates[i][j]] in rules:
                    correctly = False;
                    aux = updates[i][k];
                    updates[i].pop(k);
                    updates[i].insert(j, aux);
                    j = j - 1;
                    break;
            j = j + 1;
        if not correctly:
            sum = sum + int(updates[i][int(len(updates[i])/2)])
    print(sum);