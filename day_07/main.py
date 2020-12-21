from collections import defaultdict
def read_file():
    with open("input_final.txt") as raw_list:
        custom_form_groups = raw_list.read().rstrip().split('\n')
        return custom_form_groups

def parse_rule(rule):
    sr = rule.split(' bags contain ')
    outer_bag = sr[0]
    inner_bags = [' '.join(bag.split(' ')[1:3]) for bag in sr[1].split(', ')]
    return [outer_bag, inner_bags]

def parse_rule_form(input):
    parsed_rules = [parse_rule(rule) for rule in input]
    return parsed_rules

def look_for_shiny(list_parsed_rules):
    bags_for_check = set()
    bags_for_check.add('shiny gold')
    accepted_bags = set()
    checked_bags = []

    while bags_for_check:
        for color_to_check in bags_for_check.copy():
            for bag in list_parsed_rules:
                if color_to_check in bag[1] and bag[0] not in checked_bags:
                    bags_for_check.add(bag[0])
                    accepted_bags.add(bag[0])
            bags_for_check.remove(color_to_check)
    return len(accepted_bags)

def parse_rule_task2(rule):
    sr = rule.split(' bags contain ')
    outer_bag = sr[0]
    inner_bags = [(int(bag.split(' ')[0].replace('no', '0')), ' '.join(bag.split()[1:3])) for bag in sr[1].split(', ')]
    return (outer_bag, inner_bags)

def parse_rule_form_task2(input):
    parsed_rules = [parse_rule_task2(rule) for rule in input]
    dict_parsed_bags = {bag[0]:bag[1] for bag in parsed_rules}
    return dict_parsed_bags

def count_shiny(dict_parsed_bags):
    bags_for_check = defaultdict(int)
    bags_for_check['shiny gold']=1
    count_bags = defaultdict(int)
    while bags_for_check:
        # print(bags_for_check, count_bags)
        bags_for_check_loop = bags_for_check.copy()
        bags_for_check = defaultdict(int)
        for bag, number in bags_for_check_loop.items():
            for inner_number, inner_bag in dict_parsed_bags[bag]:
                # print(bag, dict_parsed_bags[bag], inner_bag, inner_number)
                if inner_number!=0:
                    bags_for_check[inner_bag] += inner_number*number
                    count_bags[inner_bag] += inner_number*number
        # print('\n')
    # print(bags_for_check, count_bags)
    return sum(count_bags.values())


def main():
    input = read_file()
    list_parsed_rules = parse_rule_form(input)
    print(f"Number of possible bags: {look_for_shiny(list_parsed_rules)}")
    dict_parsed_bags = parse_rule_form_task2(input)
    print(f"Number of bags in shiny gold: {count_shiny(dict_parsed_bags)}")

if __name__ == '__main__':
    main()
