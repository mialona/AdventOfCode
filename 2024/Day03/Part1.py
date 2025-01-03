import re;

with open('input.gnumeric', 'r') as file:
    text = file.read();

    imul = [m.start() for m in re.finditer('mul\(\d+,\d+\)', text)];

    sum = 0;
    for i in imul:
        pair = text[text.find('(', i) + 1:text.find(')', i)].split(',');
        sum = sum + int(pair[0])*int(pair[1]);
    print(sum)