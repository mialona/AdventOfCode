def doit(x, ido, idont):
    j = next((i - 1 for i in range(len(idont)) if idont[i] > x), len(idont) - 1);
    if j > -1:
        ndont = idont[j];
        ndo = next((y for y in ido if ndont < y), False);
        if ndo == False or x < ndo:
            return(False)
    return(True);

import re;

with open('input.gnumeric', 'r') as file:
    text = file.read();

    imul = [m.start() for m in re.finditer('mul\(\d+,\d+\)', text)];
    ido = [m.start() for m in re.finditer('do\(\)', text)];
    idont = [m.start() for m in re.finditer('don\'t\(\)', text)];

    sum = 0;
    for i in imul:
        if doit(i, ido, idont):
            pair = text[text.find('(', i) + 1:text.find(')', i)].split(',');
            sum = sum + int(pair[0])*int(pair[1]);
    print(sum)