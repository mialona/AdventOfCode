with open('input.gnumeric', 'r') as file:
    table = [];
    for line in file:
        table.append(list(line));
    nrow = len(table);
    ncol = len(table[0]) - 1;

    sum = 0;
    for i in range(nrow):
        for j in range(ncol):
            if table[i][j] == 'X':
                # Horizontal
                if (j + 1 != ncol and table[i][j + 1] == 'M') and (j + 2 != ncol and table[i][j + 2] == 'A') and (j + 3 != ncol and table[i][j + 3] == 'S'):
                    sum = sum + 1;
                if (j - 1 != -1 and table[i][j - 1] == 'M') and (j - 2 != -1 and table[i][j - 2] == 'A') and (j - 3 != -1 and table[i][j - 3] == 'S'):
                    sum = sum + 1;
                # Vertical
                if (i + 1 != ncol and table[i + 1][j] == 'M') and (i + 2 != ncol and table[i + 2][j] == 'A') and (i + 3 != ncol and table[i + 3][j] == 'S'):
                    sum = sum + 1;
                if (i - 1 != -1 and table[i - 1][j] == 'M') and (i - 2 != -1 and table[i - 2][j] == 'A') and (i - 3 != -1 and table[i - 3][j] == 'S'):
                    sum = sum + 1;
                # Diagonal
                if (i + 1 != ncol and j + 1 != ncol and table[i + 1][j + 1] == 'M') and (i + 2 != ncol and j + 2 != ncol and table[i + 2][j + 2] == 'A') and (i + 3 != ncol and j + 3 != ncol and table[i + 3][j + 3] == 'S'):
                    sum = sum + 1;
                if (i + 1 != ncol and j - 1 != -1 and table[i + 1][j - 1] == 'M') and (i + 2 != ncol and j - 2 != -1 and table[i + 2][j - 2] == 'A') and (i + 3 != ncol and j - 3 != -1 and table[i + 3][j - 3] == 'S'):
                    sum = sum + 1;
                if (i - 1 != -1 and j - 1 != -1 and table[i - 1][j - 1] == 'M') and (i - 2 != -1 and j - 2 != -1 and table[i - 2][j - 2] == 'A') and (i - 3 != -1 and i - 3 != -1 and table[i - 3][j - 3] == 'S'):
                    sum = sum + 1;
                if (i - 1 != -1 and j + 1 != ncol and table[i - 1][j + 1] == 'M') and (i - 2 != -1 and j + 2 != ncol and table[i - 2][j + 2] == 'A') and (i - 3 != -1 and j + 3 != ncol and table[i - 3][j + 3] == 'S'):
                    sum = sum + 1;
    print(sum);