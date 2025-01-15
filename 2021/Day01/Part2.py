with open('input.gnumeric', 'r') as file:
    meas = [];
    for l in file.readlines():
        meas.append(int(l.strip()));

    summ = 0;
    for i in range(len(meas) - 3):
        if meas[i] < meas[i + 3]:
            summ += 1;
    print(summ);