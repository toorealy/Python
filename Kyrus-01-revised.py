# Hash puzzle from Kyrus

# by Jason Lewis


#USAGE:
# python3 Kyrus-01-revised.py <file>


import hashlib
import string
import sys
from os import path

def get_letter_list():
    # TODO: change to list comprehension
    letter_list = []
    alpha = '\00'
    for j in range(0, 168):
        letter_list.append(alpha)
        alpha = chr(ord(alpha) + 1)
    return letter_list

### determine the type of hash being used
def determine_hash_type(hash_in):
    if len(hash_in) == 32:
        return "md5"
    elif len(hash_in) == 40:
        return "sha1"
    elif len(hash_in) == 64:
        return "sha256"
    else:
        return "unknown"

### create md5 hash
def hash_md5(hash_in):
    return hashlib.md5(hash_in.encode(encoding='UTF-8', errors="ignore")).hexdigest()

### create md5 hash
def hash_sha1(hash_in):
    return hashlib.sha1(hash_in.encode(encoding='UTF-8', errors="ignore")).hexdigest()

### create md5 hash
def hash_sha256(hash_in):
    return hashlib.sha256(hash_in.encode(encoding='UTF-8', errors="ignore")).hexdigest()

### combined hashing tool using other hashing functions
def hash_it(words_in, hash_type):
    if hash_type == "md5":
        return hash_md5(words_in)
    elif hash_type == "sha1":
        return hash_sha1(words_in)
    elif hash_type == "sha256":
        return hash_sha256(words_in)

### read a file full of hashes
def ingest_file(file_name):
    with open(file_name) as hash:
        line = hash.read().strip().split()
        return line

### returns each line generated from decoding a list of hashes
def slice_list(hash_list, phrase):
    i = 1
    for hash in hash_list:
        tempHash = hash_it(phrase,determine_hash_type(hash))
        for letter in get_letter_list():
            try:
                phrasePlus = str(phrase) + letter
            except TypeError:
                phrasePlus = letter
            tempHash = hash_it(phrasePlus,determine_hash_type(hash))
            try:
                if tempHash in hash_list[i]:
                    phrase = phrasePlus
                    i += 1
            except (IndexError, TypeError):
                return phrase

### this will recursively brute force hash-encoded strings
def crack_clues(hash_list):
    clue = ""
    clue = slice_list(hash_list,clue)
    try:
        print (clue.split('\n')[0])
    except AttributeError:
        return 0
    try:
        if determine_hash_type(clue.split('\n')[1]) != "unknown":
            crack_clues(clue.split('\n')[1::])
    except IndexError:
        return 0

### the main function call
def main():
    if path.exists(sys.argv[1]):
        crack_clues(ingest_file(sys.argv[1]))
    else:
        print ("You need to enter a valid file as the first argument.")


if __name__== "__main__":
   main()
