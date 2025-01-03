from sympy import Eq, var;
from sympy.solvers import solve;
from sympy.core.numbers import Integer;

with open('input.gnumeric', 'r') as file:
    i = 0;
    data = [];
    lines = file.readlines();
    while i < len(lines):
        machine = [];
        line = lines[i].strip();
        machine.append([int(line[line.find('X+') + 2 : line.find(',')]), int(line[line.find('Y+') + 2 :])]);
        line = lines[i + 1].strip();
        machine.append([int(line[line.find('X+') + 2 : line.find(',')]), int(line[line.find('Y+') + 2 :])]);
        line = lines[i + 2].strip();
        machine.append([int(line[line.find('X=') + 2 : line.find(',')]) + 10000000000000, int(line[line.find('Y=') + 2 :]) + 10000000000000]);
        i = i + 4;
        data.append(machine);

    # Diophantine equation (Bézout's identity)
    sum = 0;
    for machine in data:
        result = 10**100;
        var('x y');
        eq1 = Eq(machine[0][0]*x + machine[1][0]*y, machine[2][0])
        eq2 = Eq(machine[0][1]*x + machine[1][1]*y, machine[2][1])
        sols = solve([eq1, eq2], dict = True)
        result = 0;
        if len(sols) > 0:
            for sol in sols:
                a = sol[x];
                b = sol[y];
                if a > 0 and isinstance(a, Integer) and b > 0 and isinstance(b, Integer):
                    if result == 0:
                        result = 3*a + b;
                    else:
                        result = min(result, 3*a + b)
        sum = sum + result;
    print(sum);