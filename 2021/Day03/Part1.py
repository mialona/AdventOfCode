with open('input.gnumeric', 'r') as file:
    bnums = [];
    for l in file.readlines():
        bnums.append([int(i) for i in list(l.strip())]);

    sumb = [0]*len(bnums[0]);
    for b in bnums:
        for j in range(len(b)):
            sumb[j] += b[j];

    gamma = '';
    epsilon = '';
    for k in sumb:
        gamma += str(int(k/(len(bnums)/2)));
        epsilon += str(int(k/(len(bnums)/2)) ^ 1);
    print(int(gamma, 2)*int(epsilon, 2))