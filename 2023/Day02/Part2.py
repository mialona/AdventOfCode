with open('input.gnumeric', 'r') as file:
    games = [];
    for line in file:
        row = line.strip().split(':')[1].split(';');
        game = [];
        for i in row:
            trys = i.split(',');
            red = 0;
            blue = 0;
            green = 0;
            for j in trys:
                if j.find('red') > -1 and red == 0:
                    red = int(j[0 : j.find('red') - 1]);
                if j.find('blue') > -1 and blue == 0:
                    blue = int(j[0 : j.find('blue') - 1]);
                if j.find('green') > -1 and green == 0:
                    green = int(j[0 : j.find('green') - 1]);
            game.append([red, blue, green]);
        games.append(game);

    sum = 0;
    for i in range(len(games)):
        minRed = 0;
        minBlue = 0;
        minGreen = 0;
        for g in games[i]:
            minRed = max(minRed, g[0]);
            minBlue = max(minBlue, g[1]);
            minGreen = max(minGreen, g[2]);
        sum += minRed*minBlue*minGreen;
    print(sum);