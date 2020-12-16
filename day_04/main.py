import re

def read_file():
    with open("day_4_passport_list.txt") as pass_file:
        pass_string = pass_file.read().split("\n\n")
        return [row.replace('\n', ' ').split(sep=' ') for row in pass_string]


def validate_obligatory_params_task_1(dict_line: dict, obligatory_params: list):
    try:
        [dict_line[param] for param in obligatory_params]
        return True
    except:
        return False


def validate_passport_task_1(pass_list:list , obligatory_params:dict):
    valid_list = []
    for passport in pass_list:
        try:
            passport_dict = {passport_param.split(':')[0]: passport_param.split(':')[1] for passport_param in passport }
        except IndexError:
            passport = list(filter(None, passport))
            passport_dict = {passport_param.split(':')[0]: passport_param.split(':')[1] for passport_param in passport }

        valid_list.append(validate_obligatory_params_task_1(passport_dict, obligatory_params))

    return sum(valid_list)


def validate_byr(string_to_check):
    try:
        int_string = int(string_to_check)
        return int_string>=1920 and int_string<=2002
    except ValueError:
        return False


def validate_iyr(string_to_check):
    try:
        int_string = int(string_to_check)
        return int_string>=2010 and int_string<=2020
    except ValueError:
        return False


def validate_eyr(string_to_check):
    try:
        int_string = int(string_to_check)
        return int_string>=2020 and int_string<=2030
    except ValueError:
        return False


def validate_hgt(string_to_check):

    if string_to_check.endswith('cm'):
        try:
            int_string = int(string_to_check[:-2])
            return int_string>=150 and int_string<=193
        except:
            return False
    elif string_to_check.endswith('in'):
        try:
            int_string = int(string_to_check[:-2])
            return int_string>=59 and int_string<=76
        except:
            return False
    else:
        return False


def validate_hcl(string_to_check):
    if string_to_check.startswith('#') and len(string_to_check[1:]) == 6:
        regexp = re.compile(pattern = '#[0-9a-f]{6}')
        return regexp.match(string_to_check) != None
    else:
        return False


def validate_ecl(string_to_check):
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return string_to_check in valid_ecl


def validate_pid(string_to_check):
    if len(string_to_check) == 9:
        try:
            int(string_to_check)
            return True
        except:
            return False
    else:
        return False


def validate_obligatory_params_task_2(dict_line: dict):
    return (validate_byr(dict_line['byr'])
            and validate_iyr(dict_line['iyr'])
            and validate_eyr(dict_line['eyr'])
            and validate_hgt(dict_line['hgt'])
            and validate_hcl(dict_line['hcl'])
            and validate_ecl(dict_line['ecl'])
            and validate_pid(dict_line['pid'])
            )

def validate_passport_task_2(pass_list:list , obligatory_params:dict):
    valid_list = []
    for passport in pass_list:
        try:
            passport_dict = {passport_param.split(':')[0]: passport_param.split(':')[1] for passport_param in passport }
        except IndexError:
            passport = list(filter(None, passport))
            passport_dict = {passport_param.split(':')[0]: passport_param.split(':')[1] for passport_param in passport }

        passport_valid = validate_obligatory_params_task_1(passport_dict, obligatory_params) and \
                         validate_obligatory_params_task_2(passport_dict)
        valid_list.append(passport_valid)

    return sum(valid_list)


def main():
    input = read_file()
    obligatory_params_1 = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    print(f'Number of valid passports: {validate_passport_task_1(input, obligatory_params_1)}.')
    print(f'Number of valid passports: {validate_passport_task_2(input, obligatory_params_1)}.')


if __name__ == '__main__':
    main()
