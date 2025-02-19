with open('input.gnumeric', 'r') as file:
    segments = [];
    for line in file.readlines():
        pos = line.strip().split(' -> ')
        segments.append([[int(pos[0].split(',')[0]), int(pos[0].split(',')[1])], [int(pos[1].split(',')[0]), int(pos[1].split(',')[1])]]);

    map = [];
    for i in range(1000):
        map.append([0]*1000);

    for s in segments:
        if s[0][0] == s[1][0]:
            for i in range(min(s[0][1], s[1][1]), max(s[0][1], s[1][1]) + 1):
                map[s[0][0]][i] += 1;
        elif s[0][1] == s[1][1]:
            for i in range(min(s[0][0], s[1][0]), max(s[0][0], s[1][0]) + 1):
                map[i][s[0][1]] += 1;
    sum = 0;
    for i in range(1000):
        for j in range(1000):
            if map[i][j] >= 2:
                sum += 1;
    print(sum);