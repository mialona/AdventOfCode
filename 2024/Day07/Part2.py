import copy;

def init(line):
    list = copy.deepcopy(line[1]);
    num = int(list.pop(0));
    return sum_prod(int(line[0]), num, list);

def sum_prod(test, total, list):
    if len(list) == 0:
        return test == total;
    else:
        num = int(list.pop(0));
        return sum_prod(test, total + num, copy.deepcopy(list)) or sum_prod(test, total*num, copy.deepcopy(list)) or sum_prod(test, int(str(total) + str(num)), copy.deepcopy(list));

with open('input.gnumeric', 'r') as file:
    table = [];
    for line in file:
        row = line.strip().split(':');
        table.append([row[0], row[1].split()]);

    sum = 0;
    for line in table:
        if init(line):
            sum = sum + int(line[0]);
    print(sum);