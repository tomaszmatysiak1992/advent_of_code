import copy


def read_file():
    with open("input.txt") as raw_list:
        input_txt = raw_list.read().rstrip().split('\n')
        return input_txt


def parse_file(input_txt):
    boot_code = {index: value.split(' ') for index, value in enumerate(input_txt)}
    return boot_code


def processor_task_1(input_txt):
    visited_lines = set()
    instruction_line = 0
    accumulator = 0
    while True:
        if instruction_line in visited_lines:
            return accumulator
        else:
            visited_lines.add(instruction_line)
            boot_line = input_txt[instruction_line]
            if boot_line[0] == 'nop':
                instruction_line += 1
            elif boot_line[0] == 'acc':
                accumulator += int(boot_line[1])
                instruction_line += 1
            elif boot_line[0] == 'jmp':
                instruction_line += int(boot_line[1])


def processor_task_2(input_txt):
    visited_lines = set()
    instruction_line = 0
    accumulator = 0
    while True:
        if instruction_line in visited_lines:
            return False
        elif instruction_line >= len(input_txt) - 1:
            return accumulator
        else:
            visited_lines.add(instruction_line)
            boot_line = input_txt[instruction_line]
            if boot_line[0] == 'nop':
                instruction_line += 1
            elif boot_line[0] == 'acc':
                accumulator += int(boot_line[1])
                instruction_line += 1
            elif boot_line[0] == 'jmp':
                instruction_line += int(boot_line[1])


def supervisor_task_2(input_txt):
    changed_line = 0
    while True:
        changed_input = copy.deepcopy(input_txt)
        if changed_input[changed_line][0] == 'nop':
            changed_input[changed_line][0] = 'jmp'
        elif changed_input[changed_line][0] == 'jmp':
            changed_input[changed_line][0] = 'nop'
        else:
            pass
        res = processor_task_2(changed_input)
        if res:
            return res
        changed_line += 1


def main():
    input_txt = read_file()
    input_parsed = parse_file(input_txt)
    print(processor_task_1(input_parsed))
    processor_task_2(input_parsed)
    print(supervisor_task_2(input_parsed))


if __name__ == '__main__':
    main()
