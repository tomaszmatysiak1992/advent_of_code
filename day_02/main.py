def read_file():
    with open("day_2_password_list.txt") as password_file:
        return [raw_string_line.strip().split(' ') for raw_string_line in password_file.readlines()]


def check_list_task_1(pass_list):
    valid_passwords_list = []
    for password_record in pass_list:
        if validate_password_task_1(password_record):
            valid_passwords_list.append(password_record)
    return len(valid_passwords_list)


def validate_password_task_1(password_record):
    occur_range = [int(no) for no in password_record[0].split('-')]
    occur_real = password_record[2].count(password_record[1][0])
    return occur_range[0] <= occur_real <= occur_range[1]


def check_list_task_2(pass_list):
    valid_passwords_list = []
    for password_record in pass_list:
        if validate_password_task_2(password_record):
            valid_passwords_list.append(password_record)
    return len(valid_passwords_list)


def validate_password_task_2(password_record):
    char_positions = [int(no) for no in password_record[0].split('-')]
    a, b = password_record[2][char_positions[0]-1], password_record[2][char_positions[1]-1]
    return a != b and (a == password_record[1][0] or b == password_record[1][0])


def main():
    pass_list = read_file()
    print(f'Answer to first task = {check_list_task_1(pass_list)}')
    print(f'Answer to second task = {check_list_task_2(pass_list)}')


if __name__ == '__main__':
    main()
