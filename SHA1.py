# Python 2.7 x86
# Simple SHA1 Bruteforce work with dictionary of numbers, the length of the password is known
# by @rextco
from functools import reduce
import hashlib
import itertools

TARGET_HASH = "2b3e371486dee4f954150c7863877108b7d4881d"                    # SHA1 to broke
TARGET_LENGTH = 11                                                          # Password length

def bruteforce():
    # seed = "1234567890"                                                   # seed (numbers)
    # http://datagenetics.com/blog/july42015/index.html
    # seed = "etaonhisrdlumfcgwypbvkxjqz" + "1234567890"                    # lowercase + numbers
                                                                            # is the same lowercase order altered to improve
    seed = "ketaonhisrdlumfcgwypbvxjqz" + "1234567890"                      # if you know the start letter
    seed_bytes = list(map(ord, seed))
    print("seed_bytes = %s" % seed_bytes)

    # Possible are: permutations, combinations or product
    attempts = 0
    for word_bytes in itertools.product(seed_bytes, repeat=TARGET_LENGTH):
        word_string = reduce(lambda x, y: x+y, map(chr, word_bytes))        # word_bytes to string
        hash_ = hashlib.sha1(word_string).hexdigest()                       # SHA1 of word_bytes
        # hash_ = hashlib.sha1(hash_).hexdigest()                           # SHA1 again of prev SHA1

        #  print(word_string, hash_)
        if hash_ == TARGET_HASH:
            print("\n==> Founded: word = %s | hash = %s" % (word_string, hash_))
            break

        # Just for debug to check if python is alive xD
        if attempts % (1 << 20) == 0:           # Show print every 1 << 20 attempts
            print("debug!control: word = %s | hash = %s | attempts = %d" % (word_string, hash_, attempts))

        attempts += 1

if __name__ == "__main__":
    bruteforce()

