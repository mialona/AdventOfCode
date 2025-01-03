with open('input.gnumeric', 'r') as file:
    nums = [];
    for line in file:
        row = list(line.strip());
        first = None;
        last = None;
        for i in row:
            if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                if first == None:
                    first = i;
                last = i;
        nums.append(int(first + last));

    sum = 0;
    for num in nums:
        sum += num;
    print(sum);