def read_file():
    with open("day_1_1_number_list.txt") as number_list:
        raw_string = number_list.read()
        list_string = raw_string.split('\n')
        list_string = list_string[:-1]
        list_int = [int(elem) for elem in list_string]
    return list_int

test_list = [1, 2, 3, 4, 5]

def brute_force(list):
    for no, elem in enumerate(list):
        for elem_2 in list[no + 1:]:
            if elem + elem_2 == 2020:
                return (f'{elem}, {elem_2} multiplied by each other = {elem * elem_2}')

def brute_force(list):
    for no, elem in enumerate(list):
        a = no + 1
        for no_2, elem_2 in enumerate(list[no + 1:]):

            for elem_3 in list[a + 1:]:
                if elem + elem_2 + elem_3 == 2020:
                    return (
                        f'{elem}, {elem_2}, {elem_3} multiplied by each other = '
                        f'{elem * elem_2 * elem_3}')
            a += 1


def main():
    list_int = read_file()
    print(brute_force(list_int))
    print(brute_force(list_int))

if __name__ == '__main__':
    main()
