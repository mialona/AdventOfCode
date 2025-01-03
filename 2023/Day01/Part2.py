with open('input.gnumeric', 'r') as file:
    nums = [];
    for line in file:
        row = line.strip();
        first = None;
        last = None;
        for i in range(len(row)):
            if row[i] == '1' or row[i : i + 3] == 'one':
                if first == None:
                    first = '1';
                last = '1';
            if row[i] == '2' or row[i : i + 3] == 'two':
                if first == None:
                    first = '2';
                last = '2';
            if row[i] == '3' or row[i : i + 5] == 'three':
                if first == None:
                    first = '3';
                last = '3';
            if row[i] == '4' or row[i : i + 4] == 'four':
                if first == None:
                    first = '4';
                last = '4';
            if row[i] == '5' or row[i : i + 4] == 'five':
                if first == None:
                    first = '5';
                last = '5';
            if row[i] == '6' or row[i : i + 3] == 'six':
                if first == None:
                    first = '6';
                last = '6';
            if row[i] == '7' or row[i : i + 5] == 'seven':
                if first == None:
                    first = '7';
                last = '7';
            if row[i] == '8' or row[i : i + 5] == 'eight':
                if first == None:
                    first = '8';
                last = '8';
            if row[i] == '9' or row[i : i + 4] == 'nine':
                if first == None:
                    first = '9';
                last = '9';
        nums.append(int(first + last));

    sum = 0;
    for num in nums:
        sum += num;
    print(sum);