# This is an algorithm to produce hash tables and implement hashing functions for efficient data storage and retrieval. 
# It also has 4 examples of hashing functions that can be used to store strings. 

import random
import string


def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


def empty_hash_table(N):
    return [[] for n in range(N)]


def add_to_hash_table(hash_table, item, hash_function):
    N = len(hash_table)

    hash_table[hash_function(item)] = str(item)
    return hash_table


def contains(hash_table, item, hash_function):
    N = len(hash_table)
    if hash_table[hash_function(item)] == item:
        return True 
    else: 
        return False 
    # return true if the item has already been stored in the hash_table


def remove(hash_table, item, hash_function):
    if not contains(hash_table, item, hash_function):
        raise ValueError()
    else: 
        hash_table.remove(item)
    return hash_table


def hash_str1(string):
    ans = 0
    for chr in string:
        ans += ord(chr)
    return ans


def hash_str2(string):
    ans = 0
    for chr in string:
        ans = ans ^ ord(chr)
    return ans


def hash_str3(string):
    ans = 0
    for chr in string:
        ans = ans * 128 + ord(chr)
    return ans


def hash_str4(string):
    random.seed(ord(string[0]))
    return random.getrandbits(32)
