"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    access_file = open(file_path)
    content = access_file.read()
    access_file.close()

    return content


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    words.append(None)
    # iterate through the words as pairs by index
    # chains[] = 
    for i in range(len(words) - 2):
        # create a key and value
        key = (words[i], words[i + 1])
        # print(words[i], words[i + 1])
        # values = []
        value = words[i + 2]

        if key not in chains:
            chains[key] = []
        # values.append(value)
        # print(key)
        # print(value)
        chains[key].append(value)
        
    # print(chains)
        # print(value)

    # print(chains)
    
    return chains



def make_text(chains):
    """Return text from chains."""

    # use the random's choice to pick a random key from chains.keys()
    # use list() ti convert the keys into a list
    # then use the chains.keys()

    new_key = choice(list(chains.keys()))

    # add each word to a list and join the list into a string at the end
    words = [new_key[0], new_key[1]]

    # random word we pulled out from the list 'words'
    random_word = choice(chains[new_key])

    # look up that new key in the dictionary, and pull a new random word out of the resulting list until the program raises a KeyError
    # maybe we could use a loop
    #got really stuck here, had to glance at solution for guidance:
    while random_word is not None:
        new_key = (new_key[1], random_word)
        words.append(random_word)
        random_word = choice(chains[new_key])
    
    # print(words)
    # print(random_word)

    # return a string of the words we've pulled out
    return ' '.join(words)

    

# input_path = 'green-eggs.txt'
input_path = 'jokes.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# print(chains)

# Produce random text
random_text = make_text(chains)
print(random_text)
# print(random_text)
