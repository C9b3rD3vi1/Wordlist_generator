import itertools

# wordlist generator function
def wordgen():
    for word in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=3):
        yield ''.join(word)



# call main function
if __name__ == '__main__':
    for word in wordgen():
        print(word)