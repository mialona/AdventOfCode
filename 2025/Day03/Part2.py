with open('input.gnumeric', 'r') as file:
    list1 = [];
    for line in file:
        list1.append(list(line.replace('\n', '')))

    result = 0;
    for e in list1:
        list2 = [];
        j = 0;
        oldj = 0;
        for i in range(12):
            if i != 11:
                n = max(e[j:-11 + i]);
            else:
                n = max(e[j:]);
            oldj = j;
            j = e[j:].index(n) + 1 + oldj;
            list2.append(n)
        result += int(''.join(list2));
    print(result);