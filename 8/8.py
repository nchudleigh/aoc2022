def score(trees: list, height: int, reverse: bool)-> int:
    if reverse:
        trees.reverse()
    score = 0
    for tree in trees:
        score += 1
        if tree >= height:
            return score
    return score


with open('/Users/milk/Development/aoc2022/8/input.txt') as file:
    lines = file.readlines()
    grid = []
    for line in lines:
        line = line.strip('\n')
        row = [int(char) for char in line]
        grid.append(row)


    [print(line) for line in grid]

    visible_sum = 0
    exterior_sum = 0
    scores = []
    for i, line in enumerate(grid):
        if i == 0 or i == len(grid) - 1:
            exterior_sum += len(line)
            continue

        for j, char in enumerate(line):
            if j == 0 or j == len(line) - 1:
                exterior_sum += 1
                continue

            print(
                [grid[i][row_idx] for row_idx in range(0, j)],
                [grid[i][row_idx] for row_idx in range(j+1, len(line))],
                [grid[col_idx][j] for col_idx in range(0, i)],
                [grid[col_idx][j] for col_idx in range(i+1, len(grid))]
            )

            # check row left
            row_left = [grid[i][row_idx] for row_idx in range(0, j)]
            row_right = [grid[i][row_idx] for row_idx in range(j+1, len(line))]
            column_up = [grid[col_idx][j] for col_idx in range(0, i)]
            column_down = [grid[col_idx][j] for col_idx in range(i+1, len(grid))]

            scores.append(
                sum([
                    score(row_left, grid[i][j], True)  *
                    score(row_right, grid[i][j], False) *
                    score(column_up, grid[i][j], True) *
                    score(column_down, grid[i][j], False)
                ])
            )

            # if all([row_left, row_right, column_up, column_down]):
            #     continue

            # visible_sum += 1

            
    print(max(scores))
