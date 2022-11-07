"""Count words in file."""

# import the test file
# figure out how to count each word
# output in the proper format each word

def word_count(filename):
    file = open(filename) # import the text file
    words = {} # empty dictionary to hold the words from the text file
    for line in file:
        text = line.split(' ')
        for word in text:
            word = word.rstrip() # use rstrip to remove the leading and trailing whitespace
            if word in words:
                words[word] = words[word] + 1 # incremeniting the value to the word key
            else:
                words[word] = 1 # add new key and value to dictionary
    
    for key, value in words.items():
        print(f"{key} {value}")


word_count('twain.txt')