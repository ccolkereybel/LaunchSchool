def is_double_number(number):
    string_number = str(number)
    center = len(string_number) // 2

    left_side = string_number[:center]
    right_side = string_number[center:]

    return left_side == right_side

def twice(number):
    if is_double_number(number):
        return number
    else:
        return number * 2   

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True