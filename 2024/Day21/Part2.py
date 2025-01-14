def paths(i, j, path):
    if i > 0:
        laux1 = ['v' for a in range(i)];
    elif i < 0:
        laux1 = ['^' for a in range(-i)];
    else:
        laux1 = [];
    if j > 0:
        laux2 = ['>' for b in range(j)];
    elif j < 0:
        laux2 = ['<' for b in range(-j)];
    else:
        laux2 = [];
##    if i == 0:
##        return [path + laux2];
##    elif j == 0:
##        return [path + laux1];
##    else:
##        return [path + laux1 + laux2, path + laux2 + laux1];
    if i < 0:
        if j < 0:
            return [path + laux1 + laux2, path + laux2 + laux1];
        elif j > 0:
            return [path + laux2 + laux1];
        else:
            return [path + laux1];
    elif i > 0:
        if j < 0:
            return [path + laux1 + laux2];
        elif j > 0:
            return [path + laux1 + laux2, path + laux2 + laux1];
        else:
            return [path + laux1];
    else:
        return [path + laux2];

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

##with open('test.txt', 'r') as file:
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
        result = inputsnumpad(codes[i]);
        for j in range(2):
            result2 = [];
            for k in result:
                result2 += inputsdirpad(k);
            result = result2;
        for l in result:
            smin = min(smin, len(l)*numpart[i]);
        sum += smin;
    print(sum);

##    sum = 0;
##    for i in range(len(codes)):
##        smin = 10**10;
##        poss = inputsnumpad(codes[i]);
##        lposs = len(min(poss, key = len));
##        poss = [e for e in poss if len(e) == lposs];
##
##        poss2 = [];
##        for e in poss:
##            poss2 += inputsdirpad(e);
##        lposs2 = len(min(poss2, key = len));
##        poss2 = [e for e in poss2 if len(e) == lposs2];
##
##        poss3 = [];
##        for e in poss2:
##            poss3 += inputsdirpad(e);
##        lposs3 = len(min(poss3, key = len));
##
##        sum += lposs3*numpart[i];
##    print(sum);