# Wordlist generator script
# This script generates a wordlist based on the provided character set and word length range.
import os
import sys
import csv
import json
import time
import enchant
import itertools
from colorama import Fore, Style

# Character set to generate words
chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

# Min and max word length
min_length = 2
max_length = 3

# Wordlist file path to save the generated wordlist
file_path = 'wordlist'

# Enchant dictionary
dictionary = enchant.Dict("en_US")


# Wordlist generator function
def CreateWordList(chars, min_length=1, max_length=3):
    """
    Generate a wordlist based on the provided character set and word length range.

    :param chars: The character set to use (e.g., 'abc123').
    :param min_length: Minimum word length.
    :param max_length: Maximum word length.
    :yield: Words generated based on the criteria.
    """
    if min_length > max_length:
        print(Fore.RED + "[!] `min_length` must be smaller or equal to `max_length`." + Style.RESET_ALL)
        sys.exit()

    for length in range(min_length, max_length + 1):
        for word_tuple in itertools.product(chars, repeat=length):
            word = ''.join(word_tuple)
            if dictionary.check(word):  # Check if the word is valid
                yield word


# Save the generated wordlist to a file
def save_wordlist(chars, min_length, max_length, file_path, file_format='txt'):
    """
    Save the wordlist to a file in the specified format.

    :param chars: Character set for wordlist generation.
    :param min_length: Minimum word length.
    :param max_length: Maximum word length.
    :param file_path: Path to save the wordlist.
    :param file_format: File format (e.g., 'text', 'json', 'csv').
    """
    if os.path.exists(file_path):
        print(Fore.YELLOW + "File already exists. Do you want to overwrite it? (y/n)" + Style.RESET_ALL)
        choice = input("Your choice (y/n): ").strip().lower()
        if choice != 'y':
            print(Fore.RED + "Exiting without overwriting." + Style.RESET_ALL)
            return

    print(Fore.GREEN + f"Saving wordlist to {file_path} in {file_format} format..." + Style.RESET_ALL)

    # Generate the wordlist
    wordlist = list(CreateWordList(chars, min_length, max_length))

    # Save based on the specified format
    if file_format == 'text':
        with open(file_path, 'w') as f:
            f.write('\n'.join(wordlist))
    elif file_format == 'json':
        with open(file_path, 'w') as f:
            json.dump(wordlist, f, indent=4)
    elif file_format == 'csv':
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            for word in wordlist:
                writer.writerow([word])
    else:
        print(Fore.RED + f"Unsupported file format: {file_format}" + Style.RESET_ALL)

    print(Fore.GREEN + f"Wordlist saved to {file_path} in {file_format} format." + Style.RESET_ALL)



# Main function to generate and save the wordlist
if __name__ == '__main__':
    print(Fore.BLUE + f"Generating valid words from length {min_length} to {max_length}..." + Style.RESET_ALL)

    # Sleep for 6 seconds
    time.sleep(6)

    # Ask the user to enter the desired file format
    print(Fore.YELLOW + "Enter the file format to save the wordlist (text, json, csv):" + Style.RESET_ALL)

    # Get the file format from the user
    file_format = input("Your choice (text, json, csv): ").strip().lower()

    # validate the file format
    print(Fore.YELLOW + f"Validating file format: {file_format}..." + Style.RESET_ALL)

    # Sleep for 2 seconds
    time.sleep(2)

    # Validate the file format
    if file_format not in ['text', 'json', 'csv']:
        print(Fore.RED + "Invalid file format. Exiting..." + Style.RESET_ALL)
        sys.exit()
        

    print(Fore.GREEN + "Calling the save function..." + Style.RESET_ALL)
    save_wordlist(chars, min_length, max_length, file_path, file_format)
