
import sys
import os
import enchant
import itertools

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

# min and max word length 
min_length = 3
max_length = 10

# wordlist file path to save the generated wordlist
file_path = 'wordlist.txt'

# enchant dictionary
dictionary = enchant.Dict("en_US")

# set to store valid words
valid_words = set()


# wordlist generator function
def CreateWordList(chars, min_length=1, max_length=3):
    """
    Generate a wordlist based on the provided character set and word length range.

    :param chars: The character set to use (e.g., 'abc123').
    :param min_length: Minimum word length.
    :param max_length: Maximum word length.
    :yield: Words generated based on the criteria.
    """

    # Check if min_length is greater than max_length and raise an error if so.
    if min_length > max_length:
        print ("[!] Please `min_length` must smaller or same as with `max_length`")
        sys.exit()

    # Generate words based on the character set and word length range.
    for length in range(min_length, max_length + 1):
        for word in itertools.product(chars, repeat=length):
            yield ''.join(word)

        # check if generated word is valid,if valid, add to valid_words set
            if dictionary.check(''.join(word)):
                valid_words.add(''.join(word))




# save wordlist to file
def wordgen_save(file_path):

    """
    Check if the file exists; if not, create it.

    :param file_path: The path of the file to check or create.
    """
    if not os.path.exists(file_path):

        print('File does not exist. Creating a new file.')  

        with open(file_path, 'w') as f:
            for word in wordgen():
                f.write(valid_words + '\n')
    else:
        print('File already exists.')
        print('Do you want to overwrite the file? (y/n)')

        # Ask user for confirmation to overwrite the file if needed.
        choice = input()
        # If user confirms, overwrite the file.
        if choice.lower() == 'y':
            print('Overwriting the file.')
            with open(file_path, 'w') as f:
                for word in wordgen():
                    f.write(valid_words + '\n')
        else:
            print('File not overwritten.')
            print('Exiting the program.')
            exit()
        

            

# call main function
if __name__ == '__main__':
    # Generate and print words within the specified length range
    print('Words within length range {} to {}:'.format(min_length, max_length))
    print('-------------------------')

    for word in wordgen(chars, min_length, max_length):
        print(valid_words)
    
    # Uncomment to save the wordlist to a file
    wordgen_save(file_path)
