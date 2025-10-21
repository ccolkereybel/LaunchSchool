def is_color_valid(color):
    return color == "blue" or color == "green"

print(is_color_valid('blue'))

def is_color_valid(color):
    return color in ['blue', 'green']

print(is_color_valid('blue'))