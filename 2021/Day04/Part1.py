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

    for num in nums:
        for i in range(len(boards)):
            mark(boards[i], marked[i], num);
            if check(marked[i]):
                print(value(boards[i], marked[i])*int(num));
                exit();