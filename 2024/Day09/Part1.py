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

    last = 0;
    for k in range(len(mem) - 1, -1, -1):
        if mem[k] != '.':
            for l in range(last, k):
                if mem[l] == '.':
                    mem[l] = mem[k];
                    mem[k] = '.';
                    last = l;
                    break;
        if last > k:
            break;

    sum = 0;
    for m in range(len(mem)):
        if mem[m] != '.':
            sum = sum + m*int(mem[m]);
    print(sum);