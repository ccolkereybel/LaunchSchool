def print_in_box(message):
    horizonal_rule = f'+-{'-' * len(message)}-+'
    empty_line = f'| {' ' * len(message)} |'
    print(horizonal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizonal_rule)

print_in_box('hello')