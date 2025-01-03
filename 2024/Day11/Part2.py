from functools import cache;

@cache
def function(n, stone):
    if n == 0:
        return 1;
    else:
        if stone == '0':
            return function(n - 1, '1');
        else:
            if len(stone) % 2 == 0:
                return function(n - 1, str(int(stone[int(len(stone)/2):int(len(stone))]))) + function(n - 1, str(int(stone[0:int(len(stone)/2)])));
            else:
                return function(n - 1, str(int(stone)*2024));

with open('input.gnumeric', 'r') as file:
    stones = file.read().strip().split();

    result = 0;
    for i in stones:
        result = result + function(75, i);

    print(result);