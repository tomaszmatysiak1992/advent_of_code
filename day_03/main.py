def read_file():
    with open("day_3_tree_map.txt") as tree_map:
        return [raw_tree_map.strip().split(' ') for raw_tree_map in tree_map.readlines()]


def count_trees_task_1(input):
    r, d = 3, 1
    x, y = 0, 0
    trees_count = 0
    tree_char = '#'

    for i in range(0, len(input), d):
        point = input[y][0][x % 31]
        x += r
        y += d
        if point == tree_char:
            trees_count += 1

    return trees_count

def count_trees_task_2(input:list, movement_pattern:tuple):
    r, d = movement_pattern
    x, y = 0, 0
    trees_count = 0
    tree_char = '#'

    for i in range(0, len(input), d):
        point = input[y][0][x % 31]
        x += r
        y += d
        if point == tree_char:
            trees_count += 1

    return trees_count


def count_multiple_patterns(input, pattern_list):
    mulitply_res = 1
    for pattern in pattern_list:
        a = count_trees_task_2(input, pattern)
        mulitply_res *= a
    return mulitply_res


def main():
    input = read_file()
    pattern_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(f'There are {count_trees_task_1(input)} trees.')
    print(f'Total mulitply result of {pattern_list} = {count_multiple_patterns(input, pattern_list)}.')

if __name__ == '__main__':
    main()

