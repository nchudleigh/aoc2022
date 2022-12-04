with open('/Users/milk/Development/aoc2022/4/input.txt') as file:
    lines = file.readlines()

    ans = 0

    for line in lines:
        line = line.strip("\n")
        first_part, second_part = line.split(',')
        first_start, first_end = first_part.split('-')
        second_start, second_end = second_part.split('-')
        first_start = int(first_start)
        first_end = int(first_end)
        second_start = int(second_start)
        second_end = int(second_end)

        # part 1
        # is the first contained in the second?
        # if first_start >= second_start and first_end <= second_end:
        #     ans += 1
        #     continue
        
        # # is the second contained in the first
        # if second_start >= first_start and second_end <= first_end:
        #     ans += 1
        #     continue

        # part 2
        # is the first completely outside the second?
        if first_start > second_end or first_end < second_start:
            print("first is completely outside second")
            print(first_start, first_end, second_start, second_end)
            continue

        if second_start > first_end or second_end < first_start:
            print("second is completely outside first")
            print(first_start, first_end, second_start, second_end)
            continue
        
        print('contains')
        print(first_part, second_part)
        ans += 1
    
    print(ans)
