import itertools

# wordlist generator function
def wordgen():
    for word in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=3):
        yield ''.join(word)


# save wordlist to file
def wordgen_save():
    with open('wordlist.txt', 'w') as f:
        for word in wordgen():
            f.write(word + '\n')
            f.close()

            

# call main function
if __name__ == '__main__':
    for word in wordgen():
        print(word)