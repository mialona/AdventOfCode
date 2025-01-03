def comop(reg, op):
    if op == 0:
        return 0;
    elif op == 1:
        return 1;
    elif op == 2:
        return 2;
    elif op == 3:
        return 3;
    elif op == 4:
        return reg[0];
    elif op == 5:
        return reg[1];
    elif op == 6:
        return reg[2];
    else:
        print('Not valid');
        exit();

def run(reg, prog):
    i = 0;
    result = [];
    while i < len(prog):
        if prog[i] == 0: # adv
            reg[0] = int(reg[0]/(2**comop(reg, prog[i + 1])));
        elif prog[i] == 1: # bxl
            reg[1] = reg[1] ^ prog[i + 1];
        elif prog[i] == 2: # bst
            reg[1] = comop(reg, prog[i + 1]) % 8;
        elif prog[i] == 3: # jnz
            if reg[0] != 0:
                i = prog[i + 1] - 2;
        elif prog[i] == 4: # bxc
            reg[1] = reg[1] ^ reg[2];
        elif prog[i] == 5: # out
            result.append(comop(reg, prog[i + 1]) % 8);
        elif prog[i] == 6: # bdv
            reg[1] = int(reg[0]/(2**comop(reg, prog[i + 1])));
        else: # cdv
            reg[2] = int(reg[0]/(2**comop(reg, prog[i + 1])));
        i = i + 2;
    return result;

def fun(i, sA, prog, lnums):
    if i < len(prog):
        for j in range(8):
            A = list(sA);
            A[i] = str(j);
            nA = int(''.join(A), 8);
            result = run([nA, 0, 0], prog);

            if prog == result:
                lnums.append(int(''.join(A), 8));
            else:
                if prog[-i - 1:] == result[-i - 1:]:
                    fun(i + 1, ''.join(A), prog, lnums);

with open('input.gnumeric', 'r') as file:
    lines = file.readlines();
    prog = [int(i) for i in lines[4].strip().split(':')[1].split(',')];

    lnums = [];
    fun(0, ''.join(['0']*len(prog)), prog, lnums); #
    print(min(lnums));