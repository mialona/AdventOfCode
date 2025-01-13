def paths(i, j, path):
    result = [];
    if i > 0:
        result += paths(i - 1, j, path + ['v']);
    if i < 0:
        result += paths(i + 1, j, path + ['^']);
    if j > 0:
        result += paths(i, j - 1, path + ['>']);
    if j < 0:
        result += paths(i, j + 1, path + ['<']);
    if i == 0 and j == 0:
        return [path];
    return result;

numpad = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '#', '0', 'A'];
def inputsnumpad(buttons):
    result = [];
    baux = ['A'] + buttons;
    for i in range(len(baux) - 1):
        ver = int(numpad.index(baux[i + 1])/3) - int(numpad.index(baux[i])/3);
        hor = numpad.index(baux[i + 1]) % 3 - numpad.index(baux[i]) % 3;
        if ver < 0:
            if baux[i] == '0' and (baux[i + 1] == '1' or baux[i + 1] == '4' or baux[i + 1] == '7'):
                laux = [l + ['A'] for l in paths(ver + 1, hor, ['^'])];
            elif baux[i] == 'A' and (baux[i + 1] == '1' or baux[i + 1] == '4' or baux[i + 1] == '7'):
                laux = [l + ['A'] for l in paths(ver + 1, hor, ['^'])] + [l + ['A'] for l in paths(ver + 1, hor + 1, ['<', '^'])];
            else:
                laux = [l + ['A'] for l in paths(ver, hor, [])];
        else:
            if baux[i + 1] == '0' and (baux[i] == '1' or baux[i] == '4' or baux[i] == '7'):
                laux = [l + ['v', 'A'] for l in paths(ver - 1, hor, [])];
            elif baux[i + 1] == 'A' and (baux[i] == '1' or baux[i] == '4' or baux[i] == '7'):
                laux = [l + ['v', 'A'] for l in paths(ver - 1, hor, [])] + [l + ['v', '>', 'A'] for l in paths(ver - 1, hor - 1, [])];
            else:
                laux = [l + ['A'] for l in paths(ver, hor, [])];
        if len(result) == 0:
            result = laux;
        else:
            result = [x + y for x in result for y in laux];
    return result;

dirpad = ['#', '^', 'A', '<', 'v', '>'];
def inputsdirpad(buttons):
    result = [];
    baux = ['A'] + buttons;
    for i in range(len(baux) - 1):
        ver = int(dirpad.index(baux[i + 1])/3) - int(dirpad.index(baux[i])/3);
        hor = dirpad.index(baux[i + 1]) % 3 - dirpad.index(baux[i]) % 3;
        if ver < 0:
            if baux[i] == '<' and (baux[i + 1] == '^' or baux[i + 1] == 'A'):
                laux = [l + ['A'] for l in paths(ver, hor - 1, ['>'])];
            else:
                laux = [l + ['A'] for l in paths(ver, hor, [])];
        else:
            if baux[i + 1] == '<' and (baux[i] == '^' or baux[i] == 'A'):
                laux = [l + ['<', 'A'] for l in paths(ver, hor + 1, [])];
            else:
                laux = [l + ['A'] for l in paths(ver, hor, [])];
        if len(result) == 0:
            result = laux;
        else:
            result = [x + y for x in result for y in laux];
    return result;

with open('input.gnumeric', 'r') as file:
    lines = file.readlines();
    codes = [];
    numpart = [];
    for l in lines:
        codes.append(list(l.strip()));
        numpart.append(int(l[:3]));

    sum = 0;
    for i in range(len(codes)):
        smin = 10**10;
        for j in inputsnumpad(codes[i]):
            for k in inputsdirpad(j):
                for l in inputsdirpad(k):
                    smin = min(smin, len(l)*numpart[i])
        sum += smin;
    print(sum);