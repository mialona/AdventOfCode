with open('input.gnumeric', 'r') as file:
    list1 = [];
    for line in file:
        list1.append(list(line[:-1]))

    result = 0;
    n = len(list1);
    m = len(list1[0]);
    sum1 = None;
    while sum1 != 0:
        sum1 = 0;
        list2 = [[] for i in range(n)];
        for i in range(n):
            for j in range(m):
                if list1[i][j] == "@":
                    empty = 0;
                    if i == 0 or j == 0 or list1[i - 1][j - 1] != "@":
                        empty += 1;
                    if i == 0 or list1[i - 1][j] != "@":
                        empty += 1;
                    if i == 0 or j == m - 1 or list1[i - 1][j + 1] != "@":
                        empty += 1;
                    if j == 0 or list1[i][j - 1] != "@":
                        empty += 1;
                    if j == m - 1 or list1[i][j + 1] != "@":
                        empty += 1;
                    if i == n - 1 or j == 0 or list1[i + 1][j - 1] != "@":
                        empty += 1;
                    if i == n - 1  or list1[i + 1][j] != "@":
                        empty += 1;
                    if i == n - 1 or j == m - 1 or list1[i + 1][j + 1] != "@":
                        empty += 1;
                    if empty > 4:
                        sum1 += 1;
                        list2[i].append("x");
                    else:
                        list2[i].append(list1[i][j]);
                else:
                    list2[i].append(list1[i][j]);
        result += sum1;
        list1 = list2;
    print(result);