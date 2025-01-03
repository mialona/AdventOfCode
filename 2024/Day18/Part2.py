with open('input.gnumeric', 'r') as file:
    bpos = [];
    lines = file.readlines();
    for line in lines:
        baux = line.strip().split(',');
        bpos.append([int(baux[0]), int(baux[1])]);

    xmax = 70;
    ymax = 70;
    memory = [];
    for j in range(xmax + 1):
        memory.append(['.']*(ymax + 1));

    i = 0;
    while i < len(bpos):
        memory[bpos[i][0]][bpos[i][1]] = '#';

        out = [];
        for j in range(xmax + 1):
            out.append(['#']*(ymax + 1));
        out[0][0] = 0;

        laux = [[0,0]];
        while len(laux) != 0:
            newlaux = [];
            for b in laux:
                if b[0] - 1 >= 0 and memory[b[0] - 1][b[1]] != '#' and (out[b[0] - 1][b[1]] == '#' or out[b[0] - 1][b[1]] > out[b[0]][b[1]] + 1):
                    out[b[0] - 1][b[1]] = out[b[0]][b[1]] + 1;
                    newlaux.append([b[0] - 1, b[1]]);
                if b[0] + 1 < len(memory) and memory[b[0] + 1][b[1]] != '#' and (out[b[0] + 1][b[1]] == '#' or out[b[0] + 1][b[1]] > out[b[0]][b[1]] + 1):
                    out[b[0] + 1][b[1]] = out[b[0]][b[1]] + 1;
                    newlaux.append([b[0] + 1, b[1]]);
                if b[1] - 1 >= 0 and memory[b[0]][b[1] - 1] != '#' and (out[b[0]][b[1] - 1] == '#' or out[b[0]][b[1] - 1] > out[b[0]][b[1]] + 1):
                    out[b[0]][b[1] - 1] = out[b[0]][b[1]] + 1;
                    newlaux.append([b[0], b[1] - 1]);
                if b[1] + 1 < len(memory[0]) and memory[b[0]][b[1] + 1] != '#' and (out[b[0]][b[1] + 1] == '#' or out[b[0]][b[1] + 1] > out[b[0]][b[1]] + 1):
                    out[b[0]][b[1] + 1] = out[b[0]][b[1]] + 1;
                    newlaux.append([b[0], b[1] + 1]);
            laux = newlaux;

        if out[xmax][ymax] == '#':
            break;
        else:
            i += 1;

    print(bpos[i]);