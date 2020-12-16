def read_file():
    with open("day_5.txt") as raw_list:
        seat_list = raw_list.read().split('\n')
        seat_list.pop()
        return seat_list


def extract_seat_id(seat_string):
    row = seat_string[:7]
    column = seat_string[7:10]

    binary_string_prefix = '0b'
    row_binary =  binary_string_prefix+ row.replace('F', '0').replace('B', '1')
    column_binary = binary_string_prefix+ column.replace('L', '0').replace('R', '1')

    row_int = int(row_binary, base=2)
    column_int = int(column_binary, base=2)

    seat_number = 8*row_int + column_int

    return seat_number


def find_max_seat_id(seat_list):
    max_seat_id = 0

    for seat_string in seat_list:
        seat_id = extract_seat_id(seat_string)
        if seat_id>max_seat_id:
            max_seat_id = seat_id

    return max_seat_id


def create_seat_ordered_list(seat_list):
    seat_unordered_list = []
    for seat_string in seat_list:
        seat_unordered_list.append(extract_seat_id(seat_string))
    seat_ordered_list = sorted(seat_unordered_list)

    return seat_ordered_list


def find_my_seat(seat_ordered_list):
    current_seat = seat_ordered_list[0]
    for seat in seat_ordered_list[1:]:
        if current_seat== seat-1:
            current_seat = seat
        else:
            return seat-1


def main():
    input = read_file()
    print(find_max_seat_id(input))
    seat_ordered_list = create_seat_ordered_list(input)
    print(find_my_seat(seat_ordered_list))

if __name__ == '__main__':
    main()
