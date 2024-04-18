def count_line_file(filename):
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() and not line.strip().startswith('T'):
                count += 1
    return count

filename = "JourneyWith_Python/interview-preparation/file-manipulation/story.txt"
count_line_T = count_line_file(filename)
print(f"Number of lines not starting with 'T': {count_line_T}")