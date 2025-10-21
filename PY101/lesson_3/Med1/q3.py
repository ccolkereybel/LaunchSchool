def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

print(add_to_rolling_buffer1([1,2,3], 10, 5))

#one solution uses the append method, and one uses concatenation to return new list.
#solution 1 mutates orinal list, solution 2 creates new object