def read_file():
    with open("input.txt") as raw_list:
        custom_form_groups = raw_list.read().split('\n\n')
        return custom_form_groups


def count_distinct_in_group_t1(group):
    unique_answers = set(group.replace('\n', ''))
    return len(unique_answers)


def count_distinct_in_group_t2(group):
    persons_answers = group.strip().split('\n')
    return len(set.intersection(*map(set, persons_answers)))


def count_total_sum(unit_count_function, input):
    return sum(map(unit_count_function, input))


def main():
    input = read_file()
    print(f'Sum of counts {count_total_sum(count_distinct_in_group_t1, input)}')
    print(f'Sum of counts {count_total_sum(count_distinct_in_group_t2, input)}')


if __name__ == '__main__':
    main()
