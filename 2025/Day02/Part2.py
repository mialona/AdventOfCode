with open('input.gnumeric', 'r') as file:
    list1 = [];
    for line in file:
        for i in line.split(','):
            list1.append(i.split('-'))

    result = 0;
    for e in list1:
        list2 = [];
        for n in range(int(e[0]), int(e[1]) + 1):
            num = str(n);
            for d in range(2, len(num) + 1):
                if len(num) % d == 0:
                    aux1 = num[:int(len(num)/d)];
                    aux2 = True;
                    j = 1
                    while (j < d) and aux2:
                        if aux1 != num[int(len(num)/d)*j:int(len(num)/d)*(j + 1)]:
                            aux2 = False;
                            break;
                        j += 1;
                    if aux2:
                        list2.append(n);
        result += sum(set(list2));
    print(result);