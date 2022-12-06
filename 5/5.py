#     [W]         [J]     [J]        
#     [V]     [F] [F] [S] [S]        
#     [S] [M] [R] [W] [M] [C]        
#     [M] [G] [W] [S] [F] [G]     [C]
# [W] [P] [S] [M] [H] [N] [F]     [L]
# [R] [H] [T] [D] [L] [D] [D] [B] [W]
# [T] [C] [L] [H] [Q] [J] [B] [T] [N]
# [G] [G] [C] [J] [P] [P] [Z] [R] [H]
#  1   2   3   4   5   6   7   8   9 
# format the above into a list of lists
stacks = [
    [char for char in stack]
    for stack in 
   ("WRTG",
   "WVSMPHCG",
   "MGSTLC",
   "FRWMDHJ",
   "JFWSHLQP",
   "SMFNDJP",
   "JSCGFDBZ",
   "BTR",
   "CLWNH")
]


with open('/Users/milk/Development/aoc2022/5/input.txt') as file:
    lines = file.readlines()
    
    for line in lines:
        _, count, _, from_idx, _, to_idx = line.strip('\n').split(' ')
        count_idx = int(count)
        from_idx = int(from_idx) - 1
        to_idx = int(to_idx) - 1

        print(count, to_idx, from_idx)

        values = stacks[from_idx][:count_idx]
        del stacks[from_idx][:count_idx]
        # part 1
        # for value in values:
        #     stacks[to_idx].insert(0, value)

        # part 2
        stacks[to_idx] = values + stacks[to_idx]
        print(stacks[to_idx])


    print("".join([stack[0] for stack in stacks if len(stack) > 0]))
