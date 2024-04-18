def count_words(filename):
    total_words = 0

    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            total_words += len(words)

    return total_words

filename = "/home/spi_web/EXTRA/interview-prep-PYTHON/JourneyWith_Python/interview-preparation/file-manipulation/story.txt"
count_words_t = count_words(filename)
print(f"Number of words: {count_words_t}")