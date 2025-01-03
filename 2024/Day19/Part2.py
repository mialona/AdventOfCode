from functools import *;

@cache
def check(d, ps):
    num = 0;
    for p in ps:
        if d == p:
            num += 1;
        elif d[:len(p)] == p:
            num += check(d[len(p):], ps);
    return num;

with open('input.gnumeric', 'r') as file:
    lines = file.readlines();
    patterns = [];
    for p in lines[0].strip().split(','):
        patterns.append(tuple(list(p.strip())));
    designs = [];
    i = 2;
    while i < len(lines):
        designs.append(list(lines[i].strip()))
        i += 1;

    sum = 0;
    for d in designs:
        sum += check(tuple(d), tuple(patterns)); # Use of hashable objects (tuples)
    print(sum);