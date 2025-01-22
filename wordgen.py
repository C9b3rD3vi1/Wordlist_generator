
import sys
import os
import enchant
import itertools
from colorama import Fore, Back, Style

# character set to generate words
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
        print (Fore.RED + "[!] Please `min_length` must smaller or same as with `max_length`" + Style.RESET_ALL)
        sys.exit()

    # Generate words based on the character set and word length range.
    for length in range(min_length, max_length + 1):
        for word_tuple in itertools.product(chars, repeat=length):
            word = ''.join(word_tuple)
            if dictionary.check(word):  # Check if the word is valid
                yield word



# save wordlist to file
def wordgen_save(file_path, chars, min_length, max_length):
    """
    Save valid words to a file.

    :param file_path: Path to the file to save the words.
    :param chars: Character set for generating words.
    :param min_length: Minimum word length.
    :param max_length: Maximum word length.
    """
    if os.path.exists(file_path):
        print(Fore.YELLOW + "File already exists. Do you want to overwrite it? (y/n)" + Style.RESET_ALL)
        choice = input().strip().lower()
        if choice != 'y':
            print(Fore.RED + "Exiting without overwriting." + Style.RESET_ALL)
            return

    # Create or overwrite the file
    print(Fore.GREEN + "Saving valid words to the file..." + Style.RESET_ALL)
    with open(file_path, 'w') as f:
        for word in CreateWordList(chars, min_length, max_length):
            f.write(word + '\n')
    print(Fore.GREEN + f"Wordlist saved to {file_path}." + Style.RESET_ALL)
        
            

if __name__ == '__main__':

    print(Fore.BLUE + f"Generating valid words from length {min_length} to {max_length}..." + Style.RESET_ALL)
    for word in CreateWordList(chars, min_length, max_length):
        print(word)  # Print valid words to the console

    # Save to file
    wordgen_save(file_path, chars, min_length, max_length)
