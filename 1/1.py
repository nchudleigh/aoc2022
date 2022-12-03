import string

with open('./input.txt') as f:
    lines = f.readlines()
    i = 0
    elves = []
    esum = 0
    for line in lines:
        print(line)
        try:
            esum += int(line.strip(string.ascii_letters))
        except:
            elves.append(esum)
            esum = 0

    print(max(elves))
    elves.sort()
    print(elves[:-2])
    # select the last 3 elves from the list
    print(sum(elves[-3:]))
            
