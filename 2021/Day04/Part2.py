def mark(board, marked, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                marked[i][j] = 1;

def check(marked):
    markedT = [list(i) for i in zip(*marked)];
    for i in range(5):
        if sum(marked[i]) == 5 or sum(markedT[i]) == 5:
            return True;
    return False;

def value(board, marked):
    result = 0;
    for i in range(5):
        for j in range(5):
            if marked[i][j] == 0:
                result += int(board[i][j]);
    return result;

with open('input.gnumeric', 'r') as file:
    nums = file.readline().strip().split(',');
    lines = file.readlines()[1:];
    i = 0;
    boards = [];
    while i < len(lines):
        aux = [];
        aux.append(lines[i].strip().split());
        aux.append(lines[i + 1].strip().split());
        aux.append(lines[i + 2].strip().split());
        aux.append(lines[i + 3].strip().split());
        aux.append(lines[i + 4].strip().split());
        boards.append(aux);
        i += 6;
    marked = [];
    for i in range(len(boards)):
        aux = [];
        for j in range(5):
            aux.append([0]*5)
        marked.append(aux);

    last_i = None;
    last_num = None;
    l_index = range(len(boards));
    for num in nums:
        new_l_index = [];
        for i in l_index:
            mark(boards[i], marked[i], num);
            if check(marked[i]):
                last_i = i;
                last_num = num;
            else:
                new_l_index.append(i);
        l_index = list(new_l_index);
    print(value(boards[last_i], marked[last_i])*int(last_num));