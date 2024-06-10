"""Count words in file."""

def count_words(file_name):
    word_counts = {}
    file = open(file_name)

    for line in file: #gives us entire line from file
        line = line.rstrip()

        words = line.split() # returns list of individual words
        print(words)
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    # close(file)
    return word_counts

word_count_list = count_words('test.txt').items()
# print(word_count_list) #-> keys only
for line, count in word_count_list:
    print(line, count)
