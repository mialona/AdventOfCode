with open('input.gnumeric', 'r') as file:
    list1 = [];
    for line in file:
        for i in line.split(','):
            list1.append(i.split('-'))

    result = 0;
    for e in list1:
        for n in range(int(e[0]), int(e[1]) + 1):
            num = str(n);
            if len(num) % 2 == 0:
                if num[:int(len(num)/2)] == num[int(len(num)/2):]:
                    result += n;
    print(result);