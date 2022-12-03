from string import ascii_letters

with open('/Users/milk/Development/aoc2022/3/input.txt') as f:
    lines = f.readlines()
    rucksacks = []

    current_group = []
    for line in lines:
        line = line.strip("\n")

        if len(current_group) == 3:
            current_group = [line]
            continue

        if len(current_group) < 3:
            current_group.append(line)
            if len(current_group) < 3:
                continue

        e1,e2,e3 = current_group

        for char in e1:
            if char in e2 and char in e3:
                rucksacks.append(char)
                break



        # line_length = len(line)
        # compartment_1 = line[:line_length//2]
        # compartment_2 = line[line_length//2:]
        
        
        # for char in compartment_1:
        #     if char in compartment_2:
        #         rucksacks.append(char)
        #         break

    print(rucksacks)
    print(len(lines)//3)
    print(len(rucksacks))
    rucksacks_converted = [ascii_letters.index(character)+1 for character in rucksacks]
    print(rucksacks_converted)
    print(sum(rucksacks_converted))
