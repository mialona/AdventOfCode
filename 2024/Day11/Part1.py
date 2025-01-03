with open('input.gnumeric', 'r') as file:
    stones = file.read().strip().split();

    n = 0;
    while n < 25:
        i = 0;
        while i < len(stones):
            if stones[i] == '0':
                stones[i] = '1';
            else:
                if len(stones[i]) % 2 == 0:
                    stones.insert(i + 1, str(int(stones[i][int(len(stones[i])/2):int(len(stones[i]))])));
                    stones[i] = str(int(stones[i][0:int(len(stones[i])/2)]));
                    i = i + 1;
                else:
                    stones[i] = str(int(stones[i])*2024);
            i = i + 1;
        n = n + 1;

    print(len(stones));