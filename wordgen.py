
# Wordlist generator script
# This script generates a wordlist based on the provided character set and word length range.

import csv
import json
import sys
import os
import time
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


# Save the generated wordlist to a file
def save_wordlist(word, file_path, file_format='txt',file_name='wordlist' ):
    """
    Save the wordlist to a file in the specified format.

    :param wordlist: List of words to save.
    :param file_path: Path to the file to save the words.
    :param file_format: Format to save the file in (e.g., 'text', 'json', 'csv').
    """
    if os.path.exists(file_path):
        print(Fore.YELLOW + "File already exists. Do you want to overwrite it? (y/n)" + Style.RESET_ALL)
        choice = input().strip().lower()
        if choice != 'y':
            print(Fore.RED + "Exiting without overwriting." + Style.RESET_ALL)
            return

    # Save the wordlist based on the specified format
    print(Fore.GREEN + f"Saving wordlist to {file_path} in {file_format} format..." + Style.RESET_ALL)
    if file_format == 'text':
        with open(file_path, 'w') as f:
            for word in CreateWordList(chars, min_length, max_length):
                f.write(word + '\n')
    elif file_format == 'json':
        with open(file_path, 'w') as f:
            json.dump(CreateWordList, f)
    elif file_format == 'csv':
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(CreateWordList)
    print(Fore.GREEN + f"Wordlist saved to {file_path} in {file_format} format." + Style.RESET_ALL)


# Main function to generate and save the wordlist

if __name__ == '__main__':

    print(Fore.BLUE + f"Generating valid words from length {min_length} to {max_length}..." + Style.RESET_ALL)

    # sleep for 6 second
    time.sleep(6)

    #for word in CreateWordList(chars, min_length, max_length):
        #print(word)  # Print valid words to the console

    # Save to file
    print(Fore.GREEN + f"Calling the save function ........" + Style.RESET_ALL)

    save_wordlist(file_path, file_format='txt',filename='wordlist' )
