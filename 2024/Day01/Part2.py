with open('input.gnumeric', 'r') as file:
    list1 = [];
    list2 = [];
    for line in file:
        nums = line.split();
        list1.append(int(nums[0]));
        list2.append(int(nums[1]));

    sum = 0;
    for x in list1:
        sum += x*list2.count(x);
    print(sum);