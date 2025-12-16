with open('input.gnumeric', 'r') as file:
    list1 = [];
    for line in file:
        list1.append(list(line[:-1]))

    result = 0;
    for e in list1:
        n1 = max(e);
        if e.index(n1) != len(e) - 1:
            n2 = max(e[e.index(n1) + 1:])
            result += int(n1 + n2);
        else:
            auxe = list(filter((n1).__ne__, e));
            n2 = max(auxe);
            result += int(n2 + n1);
    print(result);