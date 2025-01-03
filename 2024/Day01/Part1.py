with open('input.gnumeric', 'r') as file:
    list1 = [];
    list2 = [];
    for line in file:
        nums = line.split();
        list1.append(int(nums[0]));
        list2.append(int(nums[1]));

    sum = 0;
    while len(list1) > 0:
        sum += abs(min(list1) - min(list2));
        list1.remove(min(list1));
        list2.remove(min(list2));
    print(sum);