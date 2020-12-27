from itertools import combinations


def read_file():
    with open("input_final.txt") as raw_list:
        input_txt = raw_list.read().rstrip().split('\n')
        input_int = [int(elem) for elem in input_txt]
        return input_int


def get_pairs_sum(input_txt):
    return set(map(lambda x: x[0] + x[1], combinations(input_txt, 2)))


def find_number(input_txt):
    pointer = 25
    no_elemenets = 25
    input_len = len(input_txt)
    while pointer < input_len:
        analysed_number = input_txt[pointer]
        precedessors = input_txt[pointer - no_elemenets:pointer]
        if analysed_number not in get_pairs_sum(precedessors):
            return analysed_number
        pointer += 1


def find_encryption_weakness(input_txt, weak_point_number):
    for start_elem in range(len(input_txt)):
        for finish_elem in range(start_elem + 1, len(input_txt[:])):
            continues_sum = sum(input_txt[start_elem: finish_elem + 1])
            if continues_sum == weak_point_number:
                min_number = min(input_txt[start_elem: finish_elem + 1])
                max_number = max(input_txt[start_elem: finish_elem + 1])
                return min_number + max_number
            if continues_sum > weak_point_number:
                break


def main():
    input_txt = read_file()
    print(input_txt)
    weak_point_number = find_number(input_txt)
    print(f"First number {weak_point_number}")
    print(f"Sum of min and max value = {find_encryption_weakness(input_txt, weak_point_number)}")


if __name__ == '__main__':
    main()
