with open('input.gnumeric', 'r') as file:
    table = [];
    for line in file:
        table.append(list(line));
    nrow = len(table);
    ncol = len(table[0]) - 1;

    sum = 0;
    for i in range(nrow):
        for j in range(ncol):
            if table[i][j] == 'A':
                if (i + 1 != ncol and j + 1 != ncol and table[i + 1][j + 1] == 'M') and (i - 1 != -1 and j - 1 != -1 and table[i - 1][j - 1] == 'S') and (i + 1 != ncol and j - 1 != -1 and table[i + 1][j - 1] == 'M') and (i - 1 != -1 and j + 1 != ncol and table[i - 1][j + 1] == 'S'):
                    sum = sum + 1;
                if (i + 1 != ncol and j + 1 != ncol and table[i + 1][j + 1] == 'M') and (i - 1 != -1 and j - 1 != -1 and table[i - 1][j - 1] == 'S') and (i + 1 != ncol and j - 1 != -1 and table[i + 1][j - 1] == 'S') and (i - 1 != -1 and j + 1 != ncol and table[i - 1][j + 1] == 'M'):
                    sum = sum + 1;
                if (i + 1 != ncol and j + 1 != ncol and table[i + 1][j + 1] == 'S') and (i - 1 != -1 and j - 1 != -1 and table[i - 1][j - 1] == 'M') and (i + 1 != ncol and j - 1 != -1 and table[i + 1][j - 1] == 'M') and (i - 1 != -1 and j + 1 != ncol and table[i - 1][j + 1] == 'S'):
                    sum = sum + 1;
                if (i + 1 != ncol and j + 1 != ncol and table[i + 1][j + 1] == 'S') and (i - 1 != -1 and j - 1 != -1 and table[i - 1][j - 1] == 'M') and (i + 1 != ncol and j - 1 != -1 and table[i + 1][j - 1] == 'S') and (i - 1 != -1 and j + 1 != ncol and table[i - 1][j + 1] == 'M'):
                    sum = sum + 1;
    print(sum);