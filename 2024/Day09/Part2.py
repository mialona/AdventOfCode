import copy;

with open('input.gnumeric', 'r') as file:
    data = list(file.read().strip());

    i = 0;
    mem = [];
    file = True;
    for x in data:
        if file:
            for j in range(int(x)):
                mem.append(str(i));
            i = i + 1;
            file = False;
        else:
            for j in range(int(x)):
                mem.append('.');
            file = True;

    k = len(mem) - 1;
    while k > -1:
        if mem[k] != '.':
            ksize = 1;
            while mem[k] == mem[k - ksize]:
                ksize = ksize + 1;
            l = 0;
            while l < k:
                if mem[l] == '.':
                    lsize = 1;
                    while mem[l] == mem[l + lsize]:
                        lsize = lsize + 1;
                    if (ksize <= lsize):
                        for n in range(ksize):
                            mem[l + n] = mem[k - n];
                            mem[k - n] = '.';
                        break;
                    l = l + lsize - 1;
                l = l + 1;
            k = k - ksize + 1;
        k = k - 1;

    sum = 0;
    for m in range(len(mem)):
        if mem[m] != '.':
            sum = sum + m*int(mem[m]);
    print(sum);