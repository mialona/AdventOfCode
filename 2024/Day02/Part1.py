with open('input.gnumeric', 'r') as file:
    table = [];
    for line in file:
        nums = [int(x) for x in line.split()];
        table.append(nums);

    sum = 0;
    for x in table:
        safe = True;
        if x[0] - x[1] < 0:
            for i in range(len(x) - 1):
                if x[i] - x[i+1] > 0 or abs(x[i] - x[i+1]) < 1 or abs(x[i] - x[i+1]) > 3:
                    safe = False;
        else:
            for i in range(len(x) - 1):
                if x[i] - x[i+1] < 0 or abs(x[i] - x[i+1]) < 1 or abs(x[i] - x[i+1]) > 3:
                    safe = False;
        if safe:
            sum = sum + 1;
    print(sum);