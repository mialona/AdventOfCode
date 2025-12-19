with open('input.gnumeric', 'r') as file:
    list1 = [];
    for line in file:
        list1.append(list(line[:-1]))

    result = 0;
    n = len(list1);
    m = len(list1[0]);
    for i in range(n):
        for j in range(m):
            if list1[i][j] == "@":
                empty = 0;
                if i == 0 or j == 0 or list1[i - 1][j - 1] == ".":
                    empty += 1;
                if i == 0 or list1[i - 1][j] == ".":
                    empty += 1;
                if i == 0 or j == m - 1 or list1[i - 1][j + 1] == ".":
                    empty += 1;
                if j == 0 or list1[i][j - 1] == ".":
                    empty += 1;
                if j == m - 1 or list1[i][j + 1] == ".":
                    empty += 1;
                if i == n - 1 or j == 0 or list1[i + 1][j - 1] == ".":
                    empty += 1;
                if i == n - 1  or list1[i + 1][j] == ".":
                    empty += 1;
                if i == n - 1 or j == m - 1 or list1[i + 1][j + 1] == ".":
                    empty += 1;
                if empty > 4:
                    result += 1;
    print(result);