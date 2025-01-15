with open('input.gnumeric', 'r') as file:
    bnums = [];
    for l in file.readlines():
        bnums.append([int(i) for i in list(l.strip())]);

    laux = bnums;
    for j in range(len(bnums[0])):
        laux1 = [];
        laux2 = [];
        for b in laux:
            if b[j] == 1:
                laux1.append(b);
            else:
                laux2.append(b);
        if len(laux1) > len(laux2):
            laux = laux1;
        elif len(laux1) < len(laux2):
            laux = laux2;
        else:
            laux = laux1;
        if len(laux) == 1:
            break;
    ox = int(''.join([str(k) for k in laux[0]]), 2);

    laux = bnums;
    for j in range(len(bnums[0])):
        laux1 = [];
        laux2 = [];
        for b in laux:
            if b[j] == 1:
                laux1.append(b);
            else:
                laux2.append(b);
        if len(laux1) > len(laux2):
            laux = laux2;
        elif len(laux1) < len(laux2):
            laux = laux1;
        else:
            laux = laux2;
        if len(laux) == 1:
            break;
    co2 = int(''.join([str(k) for k in laux[0]]), 2);

    print(ox*co2)