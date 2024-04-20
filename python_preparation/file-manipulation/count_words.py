def count_words(filename):
    count = 0

    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.endswith('e'):
                    count += 1

    return count

filename = "JourneyWith_Python/interview-preparation/file-manipulation/story.txt"
count_words_e = count_words(filename)
print(f"Number of lines end with 'e': {count_words_e}")