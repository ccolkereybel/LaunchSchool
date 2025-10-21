def triangle(num):
    num_of_stars = 1
    num_of_spaces = num

    for _ in range(0, num):
        print(f'{' ' * num_of_spaces}{'*' * num_of_stars}')
        num_of_spaces -= 1
        num_of_stars += 1

triangle(9)