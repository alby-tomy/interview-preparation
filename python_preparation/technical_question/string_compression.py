def compression_string(string):
    compressed_str = ""
    count = 1

    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressed_str += string[i-1]+str(count)
            count = 1

        compressed_str += string[1] + str(count)

    return compressed_str if len(compressed_str) < len(string) else string

print(compression_string("aabcccccaaa"))
