def decode_string(input_str):
    output = []
    last_char = None
    num_buffer = ''

    for char in input_str:
        if char.isalpha():
            output.append(char)
            last_char = char
            if num_buffer:  # If there's a number in the buffer, add it to output
                repeat_count = int(num_buffer)
                output.append(last_char * (repeat_count - 1))
                num_buffer = ''  # Clear the buffer after using it
        elif char.isdigit():
            num_buffer += char
        else:
            output.append(char)
            num_buffer = ''  # Clear the buffer if it's not a digit

    return ''.join(output)

# Example usage:
input1 = "a1b10"
input2 = "b3c6d15"
input3 = "ab"
input4 = "bbbccccccddddd"

print(decode_string(input1))  # Output: abbbbbbbbbb
print(decode_string(input2))  # Output: bbbccccccddddddddddddddd
print(decode_string(input3))  # Output: ab
print(decode_string(input4))  # Output: bbbccccccddddd

