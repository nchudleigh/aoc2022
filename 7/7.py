with open('/Users/milk/Development/aoc2022/7/input.txt') as file:
    lines = file.readlines()
    current_dir = []
    dir_size_map = {}
    current_size_sum = 0
    for line in lines:
        line = line.strip('\n')
        if line.startswith('$ cd'):
            if line.endswith('..'):
                current_size_sum = 0
                current_dir.pop()
            else:
                new_folder = line.replace('$ cd', '').strip()
                current_dir.append(new_folder)

        if line.startswith('$') or line.startswith('dir'):
            continue
        
        # add file size
        size, name = line.split(' ')
        file_size = int(size)

        partial_dir = []
        for directory in current_dir:
            partial_dir.append(directory)
            partial_path = '/'.join(partial_dir)
            current_size = dir_size_map.get(partial_path, 0)
            dir_size_map[partial_path] = current_size + file_size
            

    total_sum = 0
    for key, value in dir_size_map.items():
        if value <= 100_000:
            print(key, value)
            total_sum += value
    
    print('part 1:', total_sum)

    print('total space:', 70000000)
    print('total used:', dir_size_map['/'])
    print('total free:', 70000000 - dir_size_map['/'])
    print('need to free up:', 30000000 - (70000000 - dir_size_map['/']))
    need_to_free = 30000000 - (70000000 - dir_size_map['/'])

    print('part 2:', min([value for key, value in dir_size_map.items() if value >= need_to_free]))
        
