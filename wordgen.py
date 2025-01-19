import itertools

characters = 'abcdefghijklmnopqrstuvwxyz1234567890'

min_length = 3
max_length = 6


# wordlist generator function
def wordgen(characters, min_length=1, max_length=3):
    """
    Generate a wordlist based on the provided character set and word length range.

    :param chars: The character set to use (e.g., 'abc123').
    :param min_length: Minimum word length.
    :param max_length: Maximum word length.
    :yield: Words generated based on the criteria.
    """
    for length in range(min_length, max_length + 1):
        for word in itertools.product(characters, repeat=length):
            yield ''.join(word)



# save wordlist to file
def wordgen_save():
    with open('wordlist.txt', 'w') as f:
        for word in wordgen():
            f.write(word + '\n')


            

# call main function
if __name__ == '__main__':
    # Generate and print words within the specified length range
    print('Words within length range {} to {}:'.format(min_length, max_length))
    print('-------------------------')

    for word in wordgen(characters, min_length, max_length):
        print(word)
    
    # Uncomment to save the wordlist to a file
    # wordgen_save()
