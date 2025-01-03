def check(d, ps):
    valid = False;
    for p in ps:
        if d == p:
            return True;
        elif d[:len(p)] == p:
            valid = valid or check(d[len(p):], ps);
    return valid;

with open('input.gnumeric', 'r') as file:
    lines = file.readlines();
    patterns = [];
    for p in lines[0].strip().split(','):
        patterns.append(list(p.strip()))
    designs = [];
    i = 2;
    while i < len(lines):
        designs.append(list(lines[i].strip()))
        i += 1;

    sum = 0;
    for d in designs:
        if check(d, patterns):
            sum += 1;
    print(sum);