with open('input.gnumeric', 'r') as file:
    elfs = [];
    for e in file.read().split('\n\n'):
        elfs.append([int(i) for i in e.strip().split('\n')]);

    sumelf = [];
    for e in elfs:
        sumelf.append(sum(e));
    print(max(sumelf));