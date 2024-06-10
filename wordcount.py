"""Count words in file."""
import sys

command_line_filename = sys.argv[1]


def tokenize(filename):
    all_words =[]
    file = open(filename)
    for line in file:
        line = line.rstrip()
        line = line.split()
        all_words += line
    return all_words
# print(tokenize ("test.txt"))

def count_words(filename):
    word_counts = {}
    # file = open(filename) -> happens in tokenize
    all_words = tokenize(filename)
    # for word in file: #gets every word from all words
        # line = line.rstrip()
        # words = line.split() # returns list of individual words
        # print(words)
    for word in all_words:
        word_counts[word] = word_counts.get(word, 0) + 1
    # close(file)
    return word_counts

# print(count_words('test.txt'))
def print_word_counts(filename): 
    #- call count words, from that revieve dictionary of word counts
    #format print it
    word_counts = count_words(filename) #-> dictionary of word counts
    
    for word, count in word_counts.items(): 
        print(word, ", ", count)
# word_count_list = count_words(command_line_filename).items()
# print(word_count_list) #-> keys only
# for line, count in word_count_list:
#     print(line, count)

print_word_counts(command_line_filename)
